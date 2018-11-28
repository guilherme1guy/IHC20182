from django.shortcuts import render
from django.views.generic.base import TemplateView

class SearchView(TemplateView):
    template_name = "search/search.html"


class FirstPageSearchView(TemplateView):
    template_name = "search/first_page_search.html"
