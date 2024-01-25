from django.urls import path
from authorization.views import *


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]
