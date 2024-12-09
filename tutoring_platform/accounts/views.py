from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import CustomUser
from .serializers import  RegistrationSerializer , UserSerializer , LoginSerializer ,PasswordChangeSerializer
from rest_framework.permissions import AllowAny # type: ignore
from django.contrib.auth import authenticate 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token 
from rest_framework_simplejwt.views import TokenRefreshView

class TokenRefreshAPIView(TokenRefreshView):
    pass
class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self , request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"user registered successfully"} , status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # Generate or retrieve token
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutAPIView(APIView):
    def post(self, request):
        try:
            # For JWT, the logout simply means deleting the token on the client side.
            request.auth.delete()
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except AttributeError:
            return Response({"error": "No valid session found"}, status=status.HTTP_400_BAD_REQUEST)        
        

class PasswordResetRequestAPIView(APIView):
    permission_classes = [AllowAny] 
    
    def post(self ,request):
        serializer = PasswordChangeSerializer(data=request, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'detail':"password changed successfully"} ,status=status.HTTP_200_OK)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
            
            
# the profile APi          # 
# 

# student check profile complete his profile  , update 
