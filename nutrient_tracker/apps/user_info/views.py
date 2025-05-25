from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from apps.user_info.forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.


class HomeView(View):
    """View for the home page."""

    def get(self, request):
        """Handle GET requests to the home page."""
        return render(request, "home.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CreateUserForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, "login.html")


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect("home")
