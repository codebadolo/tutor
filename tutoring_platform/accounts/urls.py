# urls.py

from django.urls import path
from .views import (
    RegisterUserView,
    LoginAPIView,
    LogoutAPIView,
    PasswordResetRequestAPIView
    #PasswordResetRequestAPIView,
   # PasswordResetConfirmAPIView,
   # ChangePasswordAPIView,
    #TokenRefreshAPIView,
)

urlpatterns = [
   path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
     path('password/change/', PasswordResetRequestAPIView.as_view(), name='password_change'),
  #  path('password-reset/', PasswordResetRequestAPIView.as_view(), name='password-reset'),
   # path('password-reset/confirm/', PasswordResetConfirmAPIView.as_view(), name='password-reset-confirm'),
  #  path('password-change/', ChangePasswordAPIView.as_view(), name='password-change'),
   # path('token/refresh/', TokenRefreshAPIView.as_view(), name='token-refresh'),
]
