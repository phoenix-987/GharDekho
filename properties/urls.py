from django.urls import path
from .views import list_all_properties, list_property, add_new_property


urlpatterns = [
    path('', list_all_properties, name='get_all_properties'),
    path('<int:pk>/', list_property, name='get_property'),
    path('add-property/', add_new_property, name='add_new_property'),
]
