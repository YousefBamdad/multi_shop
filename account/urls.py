from django.urls import path
from account import views

app_name = "account"

urlpatterns = [
    path("login", views.UserLogin.as_view(), name="login"),
    path("logout", views.user_logout, name="logout"),
    path("authentication", views.UserAuthenticationView.as_view(), name="authentication"),
    path("checkotp", views.CheckOtpView.as_view(), name="checkotp"),
    path("add/address", views.AddAddressView.as_view(), name="add_address"),
]