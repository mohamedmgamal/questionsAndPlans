from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import  views
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshToken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signUp/', views.signUp, name='Registration'),
]
