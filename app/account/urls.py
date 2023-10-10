from django.urls import path
from .views import *
from django.views.generic import TemplateView



urlpatterns = [
    path('registration/', AuthCode.as_view(), name='user_registration'),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('profile/<str:email>/', UserProfile.as_view(), name='user_profile'),
    path('dead/', UserDeadView.as_view(), name='user_dead'),
    path('userdead/', UserDeadShowView.as_view(), name='userdead-list'),




 

]
