from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import CustomUser
from .serializers import  RegistrationSerializer , UserSerializer

class RegisterUserView(APIView):
    def post(self , request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"user registered successfully"} , status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self , request)  :
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data , status = status.HTTP_200_OK )
        