from .views import *
from django.urls import path


urlpatterns = [
    path('', PropertyListView.as_view(), name='get_all_properties'),
    path('<int:pk>/', GetPropertyView.as_view(), name='get_property'),
    path('add-property/', AddPropertyView.as_view(), name='add_new_property'),
    path('edit-property/<int:pk>/', EditPropertyView.as_view(), name='edit_property'),
    path('delete-property/<int:pk>/', DeletePropertyView.as_view(), name='delete_property'),
]
