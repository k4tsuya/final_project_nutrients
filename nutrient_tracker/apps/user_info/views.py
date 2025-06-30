from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from apps.user_info.forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
)
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from .forms import ContactForm
# Create your views here.


class HomeView(View):
    """View for the home page."""

    def get(self, request):
        """Handle GET requests to the home page."""
        return render(request, "index.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.success(request, "Invalid username or password.")
            return redirect("login")
    else:
        return render(request, "login.html")


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect("home")


class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
            context = {
                "u_form": u_form,
                "p_form": p_form,
            }
            return render(request, "profile.html", context)

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(
                request.POST, request.FILES, instance=request.user.profile
            )
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f"Your account has been updated!")
                return redirect("profile")


def contact_view(request):
    form = ContactForm()
    return render(request, "contact.html", {"form": form})


def about_view(request):
    return render(request, "about.html")


def ingredients_view(request):
    return render(request, "ingredients.html")


def nutrients_view(request):
    return render(request, "nutrients.html")


def recipes_view(request):
    return render(request, "recipes.html")
