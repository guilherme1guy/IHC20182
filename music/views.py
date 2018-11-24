from django.views.generic.base import TemplateView


class MyMusicView(TemplateView):
    template_name = "music/my_music.html"


class DiscoverView(TemplateView):
    template_name = "music/discover.html"
