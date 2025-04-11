import random
import string

def generate_email():
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f'test_user_{random_part}@ya.ru'

def generate_password(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))