# urls.py

from django.urls import path
from .views import (
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView,
    PasswordResetRequestAPIView,
    PasswordResetConfirmAPIView,
    ChangePasswordAPIView,
    TokenRefreshAPIView,
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('password-reset/', PasswordResetRequestAPIView.as_view(), name='password-reset'),
    path('password-reset/confirm/', PasswordResetConfirmAPIView.as_view(), name='password-reset-confirm'),
    path('password-change/', ChangePasswordAPIView.as_view(), name='password-change'),
    path('token/refresh/', TokenRefreshAPIView.as_view(), name='token-refresh'),
]
