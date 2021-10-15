from django.contrib import admin

from users.models import DeveloperProfile
from users.models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
  list_display = (
    'pk',
    'email',
    'role',
    'profile',
    'is_active',
    'last_login',
  )
  list_display_links = (
    'pk',
    'profile',
  )
  exclude = (
    'groups',
    'user_permissions',
    'password',
  )


@admin.register(DeveloperProfile)
class DeveloperProfileModelAdmin(admin.ModelAdmin):
  list_display = (
    'pk',
    'user',
    'company',
    'website',
    'phone',
  )
