from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from time import sleep

from product.models import Product


class Home(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data()
        recent_products = Product.objects.all().order_by("-created_at",)
        featured_products = Product.objects.filter(discount__gt=0)
        context['recent_products'] = recent_products[:4]
        context['featured_products'] = featured_products[:4]
        return context



@cache_page(10)
def hhome(request):
    sleep(5)
    return render(request, "home/index.html", {})
