from django.urls import path
from authorization.views import *


urlpatterns = [
    # End-point for login page.
    path('login/', UserLoginView.as_view(), name='user-login'),
    # End-point for user profile page.
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    # End-point for user registration page.
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    # End-point for change password page, so user can change it feasibly.
    path('change-password/', UserChangePasswordView.as_view(), name='user-change-password'),
]
