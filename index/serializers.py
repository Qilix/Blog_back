from rest_framework import serializers

from .models import Article, Comment


class ListArticlesSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    author = serializers.SlugRelatedField(slug_field="username", read_only=True, many=False)

    class Meta:
        model = Article
        exclude = ('text',)

class ArticleSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    author = serializers.SlugRelatedField(slug_field="username", read_only=True, many=False)

    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(read_only=True, slug_field='username')
    text = serializers.SerializerMethodField()

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text
    
    class Meta:
        model = Comment
        exlude = ("article","active")