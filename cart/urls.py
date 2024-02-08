from django.urls import path
from cart import views


app_name = "cart"
urlpatterns = [
    path("detail", views.CartDetailView.as_view(), name="cart_detail"),
    path("add/<int:pk>", views.CartAddView.as_view(), name="cart_add"),
    path("remove/<str:unique_id>", views.CartRemoveView.as_view(), name="cart_remove"),
    path("order/<int:pk>", views.OrderDetailView.as_view(), name="order_detail"),
    path("order/create", views.OrderCreationView.as_view(), name="order_create"),
    path("apply/discount/<int:pk>", views.ApplyDiscountView.as_view(), name="apply_discount"),
]