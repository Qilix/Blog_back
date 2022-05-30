from rest_framework import generics
from rest_framework.authentication import BasicAuthentication

from users.permissions import IsAuthorOrReadOnly, IsAuthor, IsAuthorComment
from .models import Article, Comment
from .serializers import CommentSerializer, ListArticlesSerializer, ArticleSerializer
from rest_framework.pagination import PageNumberPagination


class ArticleCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthor]
    authentication_classes = [BasicAuthentication]

    def perform_create(self, serializer):
	    serializer.save(author=self.request.user)

class ArticlePagination(PageNumberPagination):
    page_size = 3


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ListArticlesSerializer
    pagination_class = ArticlePagination

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthorOrReadOnly]


class CommentsView(generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthorComment]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)