from django.urls import path
from account import views

app_name = "account"

urlpatterns = [
    path("login", views.UserLogin.as_view(), name="login"),
    path("authentication", views.UserAuthenticationView.as_view(), name="authentication"),
    path("checkotp", views.CheckOtpView.as_view(), name="checkotp"),
]