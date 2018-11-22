from django.views.generic.base import TemplateView


class MyMusicView(TemplateView):
    template_name = "dashboard/my_music.html"
