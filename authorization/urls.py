from django.urls import path
from authorization.views import *


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]
