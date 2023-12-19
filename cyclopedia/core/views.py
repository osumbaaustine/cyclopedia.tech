from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Entry


class Index(TemplateView):
    template_name = "core/index.html"


class AI(ListView):
    queryset = Entry.objects
    template_name = 'core/ai.html'


def post_detail(request, slug):
    template_name = "core/details.html"
    post = get_object_or_404(Entry, slug=slug)

