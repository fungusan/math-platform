from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render

from questions.models import Topic
from questions.serializers import TopicSerializer

# Create your views here.
class TopicListView(APIView):
    def get(self, request):
        """
        Get all topic details
        """

        topics = Topic.objects.all().order_by('title')
        serializer = TopicSerializer(topics, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
