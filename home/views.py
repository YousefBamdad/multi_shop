from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from time import sleep

from product.models import Product, Offer


class Home(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data()
        recent_products = Product.objects.all().order_by("-created_at",)
        featured_products = Product.objects.filter(discount__gt=0)
        active_offers = Offer.objects.filter(is_active=True, start_date__lt=timezone.now(), end_date__gt=timezone.now())
        context['recent_products'] = recent_products[:4]
        context['featured_products'] = featured_products[:4]
        context['active_offers'] = active_offers[:2]
        return context



@cache_page(10)
def hhome(request):
    sleep(5)
    return render(request, "home/index.html", {})
