from django.urls import path
from product import views

app_name = "product"
urlpatterns = [
    path("<int:pk>", views.ProductDetailView.as_view(), name="product_detail"),
    path("shop", views.ProductListView.as_view(), name="product_list"),
    path("navbar", views.NavbarPartialView.as_view(), name="navbar"),
    path("category", views.CategoryTestView.as_view(), name="category_test"),
]