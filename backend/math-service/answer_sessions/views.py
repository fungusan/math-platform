from rest_framework.views import APIView, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import render

from answer_sessions.models import Session, UserAnswer
from answer_sessions.serializers import SessionSerializer, UserAnswerSerializer

# Create your views here.
# class SessionViewSet(viewsets.ViewSet):
