from rest_framework.views import APIView, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import F

from questions.models import Question
from questions.serializers import QuestionSerializer, ChoiceSerializer
from answer_sessions.models import Session, UserAnswer
from answer_sessions.serializers import SessionOpenSerializer, SessionEditSerializer

# Create your views here.
class SessionViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def _serialize_questions(self, questions):
        """
        for /sessions/open and /sessions/fetch
        Helper method to serialize questions with choices
        """

        serialized_questions = []

        for question in questions:
            choices_for_question = question.choice_set.all()
            choices_serializer = ChoiceSerializer(choices_for_question, many=True)
            question_data = {
                'question_id': str(question.question_id),
                'content': question.content,
                'difficulty': question.difficulty,
                'choices': [choice['choice_text'] for choice in choices_serializer.data]
            }

            serialized_questions.append(question_data)

        return serialized_questions

    def create(self, request):
        """
        Handle /sessions/open
        Create a new answer session with random questions generation
        """

        serializer = SessionOpenSerializer(data=request.data)

        if serializer.is_valid():
            # Create the session for the authenticated user
            session = Session.objects.create(
                user=request.user,
                mode=serializer.validated_data['mode'],
                start_at=timezone.now()  # Auto-set start_at
            )

            # Get parameters from validated data
            mode = serializer.validated_data['mode']
            topic_id = serializer.validated_data.get('topic_id')
            difficulty = serializer.validated_data.get('difficulty', 'medium')
            question_count = serializer.validated_data.get('question_count', 10)

            # Special business logic, always return exactly 1 question from the whole pool
            if mode == "daily":
                question_count = 1
                difficulty = 'mixed'

            # Generate random questions based on topic, difficulty, count
            questions_qs = Question.objects.all()
            if topic_id:
                questions_qs = questions_qs.filter(topic_id=topic_id)
            if difficulty != 'mixed':
                questions_qs = questions_qs.filter(difficulty=difficulty)
            # For mixed, no difficulty filter - all difficulties

            # Randomly select question_count questions (or all if fewer)
            questions = questions_qs.order_by('?')[:question_count]

            # Create UserAnswer entries for each question (answer=None)
            for question in questions:
                UserAnswer.objects.create(
                    session=session,
                    question=question,
                    answer=None  # Default null
                )

            # Serialize questions
            serialized_questions = self._serialize_questions(questions)
                            
            return Response({
                'session_id': session.session_id,
                'start_at': session.start_at,
                'questions': serialized_questions
            }, status=status.HTTP_201_CREATED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['put'])
    def edit(self, request, pk=None):
        """
        Update one answer for a unique session
        """
            
        serializer = SessionEditSerializer(data=request.data)

        if serializer.is_valid():
            try:
                # Get parameters from validated data
                question_id_to_update = serializer.validated_data['question_id']
                new_answer = serializer.validated_data['answer']

                # Get the session (enforce ownership)
                session = get_object_or_404(Session, session_id=pk, user=request.user)

                # Update the entry in UserAnswer
                answer_entry = get_object_or_404(UserAnswer, session=session, question_id=question_id_to_update)
                answer_entry.answer = new_answer
                answer_entry.save()

                return Response({"message": "Answer updated"}, status=status.HTTP_200_OK)
            
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        """
        Mark a unfinished session as finished (fill in end_at field)
        Return a list of wrong answers
        """

        try:
            # Get the session, enforce ownership
            session = get_object_or_404(Session, session_id=pk, user=request.user)

            # Check if already finished
            if session.end_at:
                return Response({"message": "Session finished already"}, status=status.HTTP_400_BAD_REQUEST)

            # Check if all questions have been answered (no null answers)
            if UserAnswer.objects.filter(session=session, answer__isnull=True).exists():
                return Response({"error": "Not all questions have been answered"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Save the end time, mark as finished
            session.end_at = timezone.now()
            session.save()

            # Complex query to get the wrong question id
            wrong_question_ids = UserAnswer.objects.filter(session=session).exclude(answer=F('question_id__answer_key')).values_list('question_id', flat=True)

            return Response({
                'end_at': session.end_at,
                'wrong_questions': list(wrong_question_ids)
            }, status=status.HTTP_200_OK)


        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
