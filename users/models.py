import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from django_countries.fields import CountryField

from knoct.utils import image_upload_to_random


class User(AbstractUser):
  """
  Represents a user on the platform, could be either a customer or a
  bussiness.
  """
  class Role(models.TextChoices):
    Developer = 'developer'
    User = 'user'

  id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False,
  )

  email = models.EmailField(
    unique=True,
    blank=False,
    editable=False,
  )

  username = models.CharField(
    max_length=128,
    null=True,
    default=None,
    editable=False,
    unique=True,
  )

  role = models.CharField(
    max_length=32,
    default=Role.User,
    choices=Role.choices,
  )

  REQUIRED_FIELDS = [
    'username',
    'first_name',
    'last_name',
  ]

  USERNAME_FIELD = 'email'

  @property
  def is_end_user(self):
    return self.role == User.Role.User

  @property
  def is_developer(self):
    return self.role == User.Role.Developer

  @property
  def name(self):
    if not self.first_name and not self.last_name:
      return None

    return self.get_full_name()

  @property
  def profile(self):
    if self.is_developer:
      return self.developer_profile

    return self.user_profile

  def __str__(self):
    return f'{self.email} {self.role}'


class UserProxyMixin:
  @property
  def email(self):
    return self.user.email

  @property
  def first_name(self):
    return self.user.first_name

  @property
  def last_name(self):
    return self.user.last_name

  @property
  def name(self):
    return self.user.name


class DeveloperProfile(UserProxyMixin, models.Model):
  """
  Represents the profile of a developer.
  """
  user = models.OneToOneField(
    User,
    related_name='developer_profile',
    on_delete=models.CASCADE,
  )

  country = CountryField(
    null=True,
    blank=True,
  )

  company = models.CharField(
    max_length=512,
    null=True,
    blank=True,
  )

  website = models.URLField(
    null=True,
    blank=True,
  )

  phone = models.CharField(
    max_length=32,
    null=True,
    blank=True,
  )

  last_updated_at = models.DateTimeField(
    auto_now=True,
  )


class UserProfile(UserProxyMixin, models.Model):
  """
  Represents the profile of a user.
  """
  user = models.OneToOneField(
    User,
    related_name='user_profile',
    on_delete=models.CASCADE,
  )

  profile_picture = models.ImageField(
    upload_to=image_upload_to_random,
    null=True,
    blank=True,
  )

  date_of_birth = models.DateField(
    null=True,
    blank=True,
  )

  country = CountryField(
    null=True,
    blank=True,
  )

  phone = models.CharField(
    max_length=32,
    null=True,
    blank=True,
  )

  last_updated_at = models.DateTimeField(
    auto_now=True,
  )

  @property
  def age(self):
    if not self.date_of_birth:
      return None

    return now() - self.date_of_birth
