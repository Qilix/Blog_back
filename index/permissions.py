from rest_framework.permissions import BasePermission
from .models import User
from rest_framework import permissions

# Проверка прав на создание
class AuthorRole(BasePermission):
    message = "Вы должны быть автором"

    def has_permission(self,request,view):
        if request.user.role != User.AUT:
            return False
        return True
        

# Проверять права для статей "только для подписчиков"
class IsAuthorOrReadOnly(permissions.BasePermission):
    message = "У вас нет доступа"

    def sub_quote(self, obj):
        return obj.sub_only == True     

    def has_object_permission(self, request, view, obj):
        if self.sub_quote(obj) and request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return True
        elif not self.sub_quote(obj):
            return True
        return obj.author == request.user