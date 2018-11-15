from django.views.generic.base import TemplateView


class SignInView(TemplateView):
    template_name = "core/sign_in.html"


class SignUpView(TemplateView):
    template_name = "core/sign_up.html"
