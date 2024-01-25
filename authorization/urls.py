from django.urls import path
from authorization.views import *


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-registration'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]
