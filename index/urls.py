from django.urls import path, include

from .views import ArticleList, ArticleDetail, UserRegister, ArticleCreate


urlpatterns = [
    path('', ArticleList.as_view()),
    path('create/', ArticleCreate.as_view()),    
    path('<int:pk>/', ArticleDetail.as_view()),
    path('user/reg/', UserRegister.as_view()),
    path('user/', include('rest_framework.urls')),
]