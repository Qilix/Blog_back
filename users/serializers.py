from rest_framework import serializers
import django.contrib.auth.password_validation as validators

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email', 'username', 'password', 'image')

    def validate(self, data):
        user = User(**data)
        password = data.get('password')
        validators.validate_password(password=password, user=user)
        return super(UserSerializer, self).validate(data)
        
    def create(self, validated_data):
            user = User(
                email=validated_data['email'],
                username=validated_data['username']
            )
            user.set_password(validated_data['password'])   
            user.save()
            return user