from django.contrib import admin

from users.models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
  list_display = ('pk', 'email', 'role', 'is_active', 'last_login')
  exclude = ('groups', 'user_permissions', 'password')
