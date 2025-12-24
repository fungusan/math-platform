from rest_framework import serializers
from questions.models import Question
from answer_sessions.models import Session, UserAnswer
from django.db import models

class SessionOpenSerializer(serializers.Serializer):  # Use Serializer, not ModelSerializer since not directly saving all fields
    mode            =   serializers.CharField(required=True)
    topic_id        =   serializers.UUIDField(required=False, allow_null=True)
    difficulty      =   serializers.ChoiceField(choices=Question.DIFFICULTY_CHOICES + [('mixed', 'Mixed')], required=False, default='medium')
    question_count  =   serializers.IntegerField(min_value=1, max_value=50, required=False, default=10)
    

class SessionEditSerializer(serializers.Serializer):
    question_id     =   serializers.UUIDField(required=True)
    answer          =   serializers.IntegerField(min_value=0, required=True)
