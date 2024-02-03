from django.urls import path
from cart import views


app_name = "cart"
urlpatterns = [
    path("detail", views.CartDetailView.as_view(), name="cart_detail"),
    path("add/<int:pk>", views.CartAddView.as_view(), name="cart_add"),
    path("remove/<str:unique_id>", views.CartRemoveView.as_view(), name="cart_remove"),
]