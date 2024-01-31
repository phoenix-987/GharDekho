from authorization.models import User
from rest_framework.permissions import BasePermission


class OwnerIsAuthenticated(BasePermission):
    """
    Custom class for Authentication specific only for owners.
    """
    def has_permission(self, request, view):
        user = User.objects.get(email=request.user)
        return bool(request.user and request.user.is_authenticated and user.is_owner)


class TenantIsAuthenticated(BasePermission):
    """
    Custom class for Authentication specific only for tenants.
    """
    def has_permission(self, request, view):
        user = User.objects.get(email=request.user)
        return bool(request.user and request.user.is_authenticated and not user.is_owner)
