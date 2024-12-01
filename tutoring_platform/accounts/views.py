from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import CustomUser
from .serializers import  RegistrationSerializer , UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate 
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self , request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"user registered successfully"} , status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    permission_classes =  [AllowAny]
    def post(self ,request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password :
            return Response({'error':'the username and password are required'} ,status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username= username , password = password )
        if user:
            refresh =  RefreshToken.for_user(user)
            return Response({
                'refresh':str(refresh),
                'access':str(refresh.access_token)
                
            })
        return Response({ "error": "invalid credentials"} , status=status.HTTP_401_UNAUTHORIZED)

class LogoutAPIView(APIView):
    def post(self, request):
        try:
            # For JWT, the logout simply means deleting the token on the client side.
            request.auth.delete()
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except AttributeError:
            return Response({"error": "No valid session found"}, status=status.HTTP_400_BAD_REQUEST)        