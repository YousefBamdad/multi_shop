from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from cart.cart_module import Cart
from product.models import Product


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, "cart/cart_detail.html", {"cart": cart})


class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        # if Example: request.POST.get("size") == None, get method will be set a default value for her = "Empty"
        size, color, quantity = request.POST.get("size", "Empty"), request.POST.get("color", "Empty"), request.POST.get("quantity")
        cart = Cart(request)
        cart.add(product=product, quantity=quantity, size=size, color=color)
        return redirect("cart:cart_detail")



class CartRemoveView(View):
    def get(self, request, unique_id):
        cart = Cart(request)
        cart.remove(unique_id)
        return redirect("cart:cart_detail")






