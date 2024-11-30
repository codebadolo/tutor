from rest_framework import serializers 
from .models import CustomUser 
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CustomUser
        fields = ['id', 'username', 'email' , 'phone_number' 'country' , 'role' , 'is_verified']
        

class  RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username' , 'email' , 'password' , 'role' , 'phone_number' , 'country']   
    
    def validate_password(self , value):
        return make_password(value)    