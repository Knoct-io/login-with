from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import FormView

from knoct.utils import templatable_errors
from users.forms import LoginViewForm


class LoginView(FormView):
  """
  View to log into the platform.
  """
  form_class = LoginViewForm
  template_name = 'auth/login/login.html'

  def form_invalid(self, form):
    return render(self.request, self.template_name, {
      'error': 'invalid credentials',
      'errors': templatable_errors(form),
    })

  def form_valid(self, form):
    user = authenticate(self.request, **form.cleaned_data)

    if not user:
      return render(self.request, self.template_name, {
        'error': 'invalid email or password',
        'form': form,
      })

    login(self.request, user)
    return redirect('/')
