from rest_framework import serializers

import django.contrib.auth.password_validation as validators

from .models import User, Article


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email', 'username', 'password')

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


class ArticleSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    author = serializers.SlugRelatedField(slug_field="username", read_only=True, many=False)

    class Meta:
        model = Article
        exclude = ('text',)

class ArticleDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    author = serializers.SlugRelatedField(slug_field="username", read_only=True, many=False)

    class Meta:
        model = Article
        fields = '__all__'