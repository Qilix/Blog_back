from django.urls import path

from .views import ArticleList, ArticleDetail, ArticleCreate


urlpatterns = [
    path('', ArticleList.as_view()),
    path('create/', ArticleCreate.as_view()),    
    path('<int:pk>/', ArticleDetail.as_view()),
]