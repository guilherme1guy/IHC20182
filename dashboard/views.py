from django.views.generic.base import TemplateView


class FeedView(TemplateView):
    template_name = "dashboard/feed.html"
