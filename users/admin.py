from django.contrib import admin

from users.models.user import User
from users.models.role import Role


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')


@admin.register(Role)
class RoleModelAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'unique_name')
