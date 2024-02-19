from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from time import sleep


class Home(TemplateView):
    template_name = "home/index.html"


@cache_page(10)
def hhome(request):
    sleep(5)
    return render(request, "home/index.html", {})
