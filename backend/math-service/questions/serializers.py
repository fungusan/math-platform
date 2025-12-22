from rest_framework import serializers
from questions.models import Question, Topic, Choice
from django.db import models

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['topic_id', 'title', 'description']
        

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['content', 'difficulty']
