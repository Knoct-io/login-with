from django.contrib import admin

from users.models import DeveloperProfile
from users.models import User
from users.models import UserProfile


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
  list_display = (
    'pk',
    'email',
    'role',
    'user_profile',
    'developer_profile',
    'is_active',
    'last_login',
  )
  list_display_links = (
    'pk',
    'user_profile',
    'developer_profile',
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
  list_display_links = (
    'pk',
    'user',
  )


@admin.register(UserProfile)
class UserProfileModelAdmin(admin.ModelAdmin):
  list_display = (
    'pk',
    'user',
    'name',
    'country',
  )
  list_display_links = (
    'pk',
    'user',
  )
