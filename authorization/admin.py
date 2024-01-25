from django.contrib import admin
from authorization.models.users import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserModelAdmin(UserAdmin):
    # Customising the view of admin panel, which fields to be shown
    list_display = ('id', 'email', 'name', 'is_owner', 'is_admin')
    # Helps to filter out data at admin panel
    list_filter = ('is_owner', 'is_admin')
    # Categorised the data acording to our need.
    fieldsets = [
        ('User Credentials', {'fields': ['email', 'password']}),
        ('Personal Info', {'fields': ['name']}),
        ('Roles', {'fields': ['is_owner', 'is_admin']}),
    ]

    add_fieldsets = [
        (
            None,
            {'fields': ('email', 'name', 'password', 'confirm_password')}
        )
    ]

    search_fields = ['email']
    ordering = ['email', 'name']


admin.site.register(User, UserModelAdmin)
