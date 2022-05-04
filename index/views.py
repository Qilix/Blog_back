from rest_framework import generics
from rest_framework.authentication import BasicAuthentication

from users.permissions import IsAuthorOrReadOnly, AuthorRole
from .models import Article
from .serializers import ListArticlesSerializer, ArticleSerializer


class ArticleCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AuthorRole]
    authentication_classes = [BasicAuthentication]

    def perform_create(self, serializer):
	    serializer.save(author=self.request.user)


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ListArticlesSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthorOrReadOnly]