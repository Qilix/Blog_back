from django.urls import path

from .views import *


urlpatterns = [
    path('', ArticleList.as_view()),
    path('create/', ArticleCreate.as_view()),    
    path('<int:pk>/', ArticleDetail.as_view()),
    path('comments/', CommentsView.as_view()),
    path('comments/<int:pk>/', CommentsView.as_view()),
]