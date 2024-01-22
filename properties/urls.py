from django.urls import path
from .views import list_all_properties, list_properties


urlpatterns = [
    path('', list_all_properties, name='home page'),
    path('<pk>/', list_properties, name='home page'),
]
