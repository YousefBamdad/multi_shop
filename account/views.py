from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from account.forms import LoginForm, RegisterForm, CheckOtpForm, AuthenticationForm, AddressCreationForm
import ghasedakpack
from random import randint
from django.utils.crypto import get_random_string
from uuid import uuid4
from account.models import Otp, User

SMS = ghasedakpack.Ghasedak("187bf878bc4924480fcab88a116fe5db5a1ea14689becd518307e3d088cc48f7")


def user_login(request):

    return render(request, "account/login.html", {})


def user_logout(request):
    logout(request)
    return redirect("home:home")


class UserLogin(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home:home")
        form = LoginForm()
        return render(request, "account/login.html", {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect("home:home")
            else:
                form.add_error("phone", "Invalid Username or Password")
        else:
            form.add_error("username", "Invalid Data!")
        return render(request, "account/login.html", {'form': form})


class UserAuthenticationView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home:home")

        form = AuthenticationForm()
        return render(request, "account/authentication.html", {'form': form})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000, 9999)
            # SMS.verification({'receptor': cd["phone"], 'type': '1', 'template': 'randomcode2007', 'param1': randcode})
            token = str(uuid4())
            Otp.objects.create(phone=cd['phone'], code=randcode, token=token)
            print(randcode)
            return redirect(reverse("account:checkotp") + f"?token={token}")
        else:
            form.add_error("phone", "Invalid Phone!")
        return render(request, "account/authentication.html", {'form': form})


class CheckOtpView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home:home")

        form = CheckOtpForm()
        return render(request, "account/check_otp.html", {'form': form})

    def post(self, request):
        token = request.GET.get("token")
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_created = User.objects.get_or_create(phone=otp.phone)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                otp.delete()
                return redirect("home:home")
        else:
            form.add_error("code", "Invalid Code!")
        return render(request, "account/check_otp.html", {'form': form})


class AddAddressView(View):
    def post(self, request):
        form = AddressCreationForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)

        print(len(request.user.addresses.all()))
        if len(request.user.addresses.all()) > 4:
            form.add_error("user", "You can register a maximum of 5 addresses")
        return render(request, 'account/add_address.html', {'form': form})

    def get(self, request):
        form = AddressCreationForm()
        return render(request, 'account/add_address.html', {'form': form})
