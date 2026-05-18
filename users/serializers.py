from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  

    class Meta:  
        model = User  
        fields = ('username', 'password', 'email', 'role')  

    def create(self, validated_data):  
        user = User.objects.create_user(  
            username=validated_data['username'],  
            password=validated_data['password'],  
            email=validated_data.get('email'),  
            role=validated_data.get('role')  
        )  
        return user  
