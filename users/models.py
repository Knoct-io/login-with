import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField


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

  def __str__(self):
    return f'{self.email} {self.role}'


class DeveloperProfile(models.Model):
  """
  Represents the profile of a developer.
  """
  user = models.OneToOneField(
    User,
    related_name='profile',
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
