from django.core.exceptions import ValidationError

class CustomPasswordValidator:
    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(('Пароль должен содержать хотя бы %(min_length)d цифру.') % {'min_length': self.min_length})
        if not any(char.isalpha() for char in password):
            raise ValidationError(('Пароль должен содержать хотя бы одну %(min_length)d букву.') % {'min_length': self.min_length})

    def get_help_text(self):
        return "Введи корректный пароль"

