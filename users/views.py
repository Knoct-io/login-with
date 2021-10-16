from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView

from knoct.utils import templatable_form_errors
from users.forms import LoginViewForm
from users.forms import RegisterViewForm
from users.models import User


class LoginView(FormView):
  """
  View to log into the platform.
  """
  form_class = LoginViewForm
  template_name = 'auth/login/login.html'

  def get(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return self.redirect_to_success()

    return super().get(request, *args, **kwargs)

  def form_invalid(self, form):
    return render(self.request, self.template_name, {
      'form': form,
      'errors': templatable_form_errors(form),
    })

  def form_valid(self, form):
    user = authenticate(self.request, **form.cleaned_data)

    if not user:
      return render(self.request, self.template_name, {
        'error': 'invalid email or password',
        'form': form,
      })

    login(self.request, user)
    return self.redirect_to_success()

  def redirect_to_success(self):
      return redirect('/')


class RegisterView(FormView):
  form_class = RegisterViewForm
  template_name = 'auth/register/register.html'

  def get(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return self.redirect_to_success()

    return super().get(request, *args, **kwargs)

  def form_invalid(self, form):
    return render(self.request, self.template_name, {
      'form': form,
      'errors': templatable_form_errors(form),
    })

  def form_valid(self, form):
    role = User.Role.User

    if form.cleaned_data.get('developer'):
      role = User.Role.Developer

    User.objects.create_user(
      first_name=form.cleaned_data.get('first_name'),
      last_name=form.cleaned_data.get('last_name'),
      role=role,
      email=form.cleaned_data.get('email'),
      password=form.cleaned_data.get('password'),
    )

    return self.redirect_to_success()

  def redirect_to_success(self):
      return redirect(reverse('login'))
