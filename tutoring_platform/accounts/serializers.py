from rest_framework import serializers 
from .models import CustomUser 
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'first_name', 'last_name', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
        def create(self , validated_data):
            user = get_user_model().objects.create_user(**validated_data)
            return user 
        
        

class  RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email' , 'password' , 'role' , 'phone_number' , 'country']   
    
    def validate_password(self , value):
        return make_password(value)     