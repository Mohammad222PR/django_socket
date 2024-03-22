from django.core.exceptions import ValidationError
from django.db import models
import re

def validate_phone_number(value):
    pattern = r'^\+989\d{9}$'
    if not re.match(pattern, value):
        raise ValidationError('شماره تلفن همراه باید با فرمت +989باشد')

def validate_national_code(value):
    pattern = r'^\d{10}$'
    if not re.match(pattern, value):
        raise ValidationError('کد ملی باید شامل 10 رقم باشد')

def validate_name(value):
    pattern = r'^[a-zA-Z]+$'
    if not re.match(pattern, value):
        raise ValidationError('نام فقط می‌تواند شامل حروف باشد')

class MyModel(models.Model):
    phone_number = models.CharField(max_length=20, validators=[validate_phone_number])
    national_code = models.CharField(max_length=10, validators=[validate_national_code])
    name = models.CharField(max_length=100, validators=[validate_name])
