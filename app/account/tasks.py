from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_otp_email(auth_code, email):
    subject = 'Добро пожаловать!!!'
    message = f'Пожалуйста подтвердите регистрацию: Ваш код подтверждения {auth_code} действителен в течении 5 минут '
    send_mail(subject, message, 'varvar1987a@mail.ru', [email], fail_silently=False)


