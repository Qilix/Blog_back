from django.urls import path, include

from .views import QuoteList, QuoteDetail, UserRegister, QuoteCreate


urlpatterns = [
    path('', QuoteList.as_view()),
    path('create/', QuoteCreate.as_view()),    
    path('<int:pk>/', QuoteDetail.as_view()),
    path('user/reg/', UserRegister.as_view()),
    path('user/', include('rest_framework.urls')),
]