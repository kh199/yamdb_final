from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone

characters_validator = RegexValidator(
    r'^[-a-zA-Z0-9_]+$',
    'Символы латинского алфавита, цифры и знак подчёркивания'
)


def year_validator(value):
    if value > timezone.now().year:
        raise ValidationError(
            'Пожалуйста, введите корректный год!'
        )
