from django.urls import path, include

from .views import UserRegister


urlpatterns = [
    path('reg/', UserRegister.as_view()),
    path('/', include('rest_framework.urls')),
]