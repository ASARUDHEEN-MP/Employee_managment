from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer
from rest_framework.permissions import AllowAny
from django.utils import timezone
from rest_framework.views import APIView
from .utils import get_tokens
from django.contrib.auth import authenticate

class RegisterView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# login

class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow access to unauthenticated users

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        if user is None:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Update last login timestamp
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])

        # Serialize user data
        serialized_data = CustomUserSerializer(user).data
        
        # Generate JWT token
        token = get_tokens(user)
        
        # Create response with HTTP-only cookie for the token
        response = Response({
            'userInfo': serialized_data,
            'token': token,
            'message': 'Successfully logged in',
            'status': status.HTTP_200_OK
        })
        response.set_cookie(key='jwt', value=token, httponly=True)

        return response
    


