import re
from django.http import JsonResponse


def validate_email(value):
    email_regex = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return re.match(email_regex, value)

def validate_phone_number(value):
    phone_regex = re.compile(r'^01([0|1]?)-?([0-9]{3,4})-?([0-9]{4})$')
    if not re.match(phone_regex, value):
        return 0
    value = re.sub("-", "", value)
    return value

def validate_password(value):
    password_regex = re.compile(r'^[a-zA-Z0-9!@#$%^&*()_+,./<>?;:`~]{8,}$')
    return re.match(password_regex, value)
