from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from cart.cart_module import Cart
from cart.models import Order, OrderItem, DiscountCode
from product.models import Product


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, "cart/cart_detail.html", {"cart": cart})


class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        # if Example: request.POST.get("size") == None, get method will be set a default value for her = "Empty"
        size, color, quantity = request.POST.get("size", "Empty"), request.POST.get("color", "Empty"), request.POST.get(
            "quantity")
        cart = Cart(request)
        cart.add(product=product, quantity=quantity, size=size, color=color)
        return redirect("cart:cart_detail")


class CartRemoveView(View):
    def get(self, request, unique_id):
        cart = Cart(request)
        cart.remove(unique_id)
        return redirect("cart:cart_detail")


# Orders
class OrderDetailView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        return render(request, 'cart/order_detail.html', {'order': order})


class OrderCreationView(View):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect("account:authentication")
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total())
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                size=item['size'],
                color=item['color'],
                quantity=item['quantity'],
                price=item['price'],
            )
        cart.remove_cart()
        return redirect("cart:order_detail", order.id)

class ApplyDiscountView(View):
    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        code = request.POST.get('discount_code')
        discount_code = get_object_or_404(DiscountCode, name=code)
        if discount_code.quantity == 0:
            return redirect("cart:order_detail", order.id)
        order.total_price -= order.total_price * (discount_code.discount / 100)
        order.save()
        discount_code.quantity -= 1
        discount_code.save()
        return redirect("cart:order_detail", order.id)
