from django.views.generic.base import TemplateView


class MyMusicView(TemplateView):
    template_name = "music/my_music.html"


class DiscoverView(TemplateView):
    template_name = "music/discover.html"


class DetailMusicView(TemplateView):
    template_name = "music/detail_music.html"


class DetailAlbumView(TemplateView):
    template_name = "music/detail_album.html"


class DetailPlaylistView(TemplateView):
    template_name = "music/detail_playlist.html"
