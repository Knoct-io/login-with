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


class RegisterViewForm(forms.Form):
  """
  Form for the register view.
  """
  first_name = User.first_name.field.formfield(
    required=True,
    validators=User.first_name.field.validators,
  )

  last_name = User.last_name.field.formfield(
    required=True,
    validators=User.last_name.field.validators,
  )

  email = User.email.field.formfield(
    required=True,
    validators=User.email.field.validators,
  )

  password = User.password.field.formfield(
    required=True,
    validators=User.password.field.validators,
  )

  developer = forms.BooleanField(
    required=False,
    initial=False,
  )

  def clean_email(self):
    email = self.cleaned_data.get('email')
    email = User.objects.normalize_email(email)

    if User.objects.filter(email=email).exists():
      raise forms.ValidationError('An account with this email already exists.')

    return email
