from django.views.generic.base import TemplateView

class SignInView(TemplateView):
    template_name = "account/sign_in.html"

class SignUpView(TemplateView):
    template_name = "account/sign_up.html"

class HelpPage(TemplateView):
    template_name = "account/help_page.html"

class InstructionPage(TemplateView):
    template_name = "account/instruction_page.html"
