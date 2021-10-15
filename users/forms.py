from django import forms

from users.models import User


class LoginViewForm(forms.Form):
  """
  Form for the login view.
  """
  email = User.email.field.formfield(
    required=True,
    validators=User.email.field.validators,
  )

  password = User.password.field.formfield(
    required=True,
    validators=User.password.field.validators,
  )
