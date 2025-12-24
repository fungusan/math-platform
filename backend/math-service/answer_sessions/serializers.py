from rest_framework import serializers
from answer_sessions.models import Session, UserAnswer
from django.db import models

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['user_id', 'start_at', 'end_at', 'mode']


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['user_id', 'start_at', 'question_id', 'answer']