from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import  views
urlpatterns = [
    path('getQuestions/<int:section>', views.getQuestions, name='getQuestions'),
    path('answer/',views.Answer,name="Answer Question in attempt"),
    path('getAttempts/',views.getAttempts,name="get getAttempts")
]
