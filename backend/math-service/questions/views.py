from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify

from questions.models import Topic, Choice, Question
from questions.serializers import TopicSerializer, QuestionSerializer, ChoiceSerializer

# Create your views here.
class TopicListView(APIView):
    def get(self, request):
        """
        Get topic list
        """

        topics = Topic.objects.all().order_by('title')
        serializer = TopicSerializer(topics, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class QuestionDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, question_slug):
        """
        Get a specific question details by slug (auth required, no answer_key)
        """
        
        try:
            question = get_object_or_404(Question, slug=question_slug)
            choices_for_question = question.choice_set.all()  # Ordered by 'order' via Meta
            
            question_serializer = QuestionSerializer(question)
            choices_serializer = ChoiceSerializer(choices_for_question, many=True)

            return Response({
                **question_serializer.data,
                'choices': [choice['choice_text'] for choice in choices_serializer.data]
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)