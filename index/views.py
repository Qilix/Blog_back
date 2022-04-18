from rest_framework import generics
from rest_framework.authentication import BasicAuthentication

from .permissions import IsAuthorOrReadOnly, AuthorRole
from .models import Article, User
from .serializers import ArticleSerializer, UserSerializer, ArticleDetailSerializer


class ArticleCreate(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [AuthorRole]
    authentication_classes = [BasicAuthentication]

    def perform_create(self, serializer):
	    serializer.save(author=self.request.user)


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
        

class UserRegister(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer