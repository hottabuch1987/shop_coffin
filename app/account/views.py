from django.utils import timezone
from datetime import timedelta
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserDeadSerializer
from .models import UserDead
from .tasks import send_otp_email
import random
import string
from django.contrib.auth import authenticate, login, get_user_model

from .models import User





class UserGithube(APIView):
    """User GitHube"""
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        auth_code = ''.join(random.choice(string.digits) for _ in range(6))
        
        user = User.objects.create(email=email, auth_code=auth_code, password=password)
        
        user.is_verified = True

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return Response({"message": "Вы успешно вошли в систему."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Неправильный адрес электронной почты или пароль."}, status=status.HTTP_401_UNAUTHORIZED)

# {"email":"varvar1987a@mail.ru",
# "password":"arik1987A"}




class UserLogin(APIView):
    """User login"""
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_verified:
            login(request, user)
            return Response({"message": "Вы успешно вошли в систему."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Неправильный адрес электронной почты или пароль."}, status=status.HTTP_401_UNAUTHORIZED)


class AuthCode(APIView):
    """Authorization by email"""
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        auth_code = request.data.get('auth_code')

        user, created = get_user_model().objects.get_or_create(email=email)

        if not created and user.is_verified:
            return Response({"message": "Пользователь уже проверен."},
                            status=status.HTTP_400_BAD_REQUEST)

        if not user.auth_code:

            auth_code = ''.join(random.choice(string.digits) for _ in range(6))

        if password:
            user.set_password(password)

        user.auth_code = auth_code
        user.auth_code_created_at = timezone.now()
        user.is_verified = False
        user.save()

        send_otp_email.delay(auth_code, email)

        return Response({"message": "Код авторизации отправлен на email.", "auth_code": auth_code},
                        status=status.HTTP_200_OK)

    def patch(self, request):
   
        auth_code = request.data.get('auth_code')

       
        user = get_user_model().objects.filter(auth_code=auth_code).first()
   

        if user.auth_code == auth_code and \
                user.auth_code_created_at + timedelta(minutes=5) >= timezone.now():
            user.is_verified = True
            user.save()
            return Response({"message": "Код авторизации подтвержден."},
                            status=status.HTTP_200_OK)
        else:
            return Response({"message": "Неверный код авторизации."},
                            status=status.HTTP_400_BAD_REQUEST)


class UserProfile(APIView):
    """User profile"""
    def get(self, request, email):
        user = get_user_model().objects.filter(email=email).first()

        if user is None:
            return Response({"message": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)

        invited_users = get_user_model().objects.filter(invite_code=user.invite_code)
        invited_emails = [invited_user.email for invited_user in invited_users]
        serializer.data['invited_emails'] = invited_emails

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, email):
        user = get_user_model().objects.filter(email=email).first()

        if user is None:
            return Response({"message": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)

        invite_code = request.data.get('invite_code')

        if invite_code and user.invite_code_used:
            return Response({"message": "Invite code already used."}, status=status.HTTP_400_BAD_REQUEST)

        user.invite_code = invite_code
        user.save()
        return Response({"message": "Invite code updated."}, status=status.HTTP_200_OK)

    def delete(request, email):
        user = get_user_model().objects.filter(email=email).first()

        if user is None:
            return Response({"message": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({"message": "Профиль успешно удален."}, status=status.HTTP_204_NO_CONTENT)


class UserDeadView(APIView):
    ''''Добавление умерших'''
    def post(self, request):
        famyli = request.data.get('famyli')
        name = request.data.get('name')
        surname = request.data.get('surname')
        user, created = UserDead.objects.get_or_create(famyli=famyli, name=name, surname=surname)


        
        if not created:
            return Response({"message": "Умерший уже базе."},
                            status=status.HTTP_400_BAD_REQUEST)
        user.save()
        return Response({"message": "Данные сохранены успешно."},
                        status=status.HTTP_200_OK)


class UserDeadShowView(APIView):
    '''Вывод умерших'''
    
    def get(self, request, format=None):
        users = UserDead.objects.all()
        serializer = UserDeadSerializer(users, many=True)
        return Response(serializer.data)


        