from django.views.generic import TemplateView


class ExampleTemplateView(TemplateView):
  template_name = 'auth/login/login.html'
