from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from users.serializers import UserSerializer, RegisterSerializer, LoginSerializer
from users.models import User

import json
from uuid import UUID

# Create your views here.
@csrf_exempt
def handle_echo(request):
    """
    Simple echo for testing communication.
    """

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            response_msg = data.get('message', '')
            response_msg += ' frontend'
            return JsonResponse({'message': response_msg})
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
    return JsonResponse({'error': 'Method not allowed'}, status=405)

class UserDetailView(APIView):
    def get(self, request, id):
        """
        Get basic information of a user by UUID.
        """

        try:
            uuid_obj = UUID(id)  # Validates and normalizes (handles with/without hyphens)
            user = get_object_or_404(User, id=uuid_obj)
            serializer = UserSerializer(user)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except ValueError:
            return Response({'error': 'Invalid UUID format'}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        """
        Register a new user, and log him/her in
        """

        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)   # Generate JWT

            # On success
            return Response({
                'token': str(refresh.access_token),
                'user': { 'id': str(user.id), 'user_name': user.user_name }
            }, status=status.HTTP_201_CREATED)
        
        # On failure
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        """
        Log user in
        """

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = authenticate(email=serializer.validated_data['email'], 
                                password=serializer.validated_data['password'])

            if user:
                refresh = RefreshToken.for_user(user)   # Generate JWT

                # On success
                return Response({
                    'token': str(refresh.access_token),
                    'user': { 'id': str(user.id), 'user_name': user.user_name }
                }, status=status.HTTP_200_OK)
            
            # On invalid credentials
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # On failure
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)