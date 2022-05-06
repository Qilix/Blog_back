from rest_framework import serializers

from .models import Article, Comment


class ListArticlesSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    author = serializers.SlugRelatedField(slug_field="username", read_only=True, many=False)

    class Meta:
        model = Article
        exclude = ('text',)


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    author = serializers.SlugRelatedField(slug_field="username", read_only=True, many=False)
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'