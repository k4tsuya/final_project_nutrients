from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.


class HomeView(View):
    """View for the home page."""

    def get(self, request):
        """Handle GET requests to the home page."""
        return render(request, "home.html")
