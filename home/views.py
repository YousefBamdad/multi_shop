from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from time import sleep

from product.models import Product


class Home(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data()
        products = Product.objects.all().order_by("-created_at",)
        context['recent_products'] = products[:4]
        return context



@cache_page(10)
def hhome(request):
    sleep(5)
    return render(request, "home/index.html", {})
