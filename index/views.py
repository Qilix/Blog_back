from rest_framework import generics

from .permissions import IsAuthorOrReadOnly, AuthorRole
from .models import Quote, User
from .serializers import QuoteSerializer, UserSerializer, QuoteDetailSerializer


class QuoteCreate(generics.CreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteDetailSerializer
    permission_classes = [AuthorRole]

    def perform_create(self, serializer):
	    serializer.save(author=self.request.user)


class QuoteList(generics.ListAPIView):
    queryset = Quote.objects.all().order_by('-created_at')
    serializer_class = QuoteSerializer


class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteDetailSerializer
    permission_classes = [IsAuthorOrReadOnly]

class UserRegister(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer