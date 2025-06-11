"""View to list nutrient trackers."""

from typing import Any

from apps.tracker_data.models import NutrientTracker
from django.db.models import QuerySet
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.


# limit who can see the nutrient tracker
class NutrientTrackerListView(ListView):
    """Class to list nutrient trackers."""

    model = NutrientTracker
    template_name: str = "nutrient_tracker_list.html"
    context_object_name: str = "nutrient_trackers"
    paginate_by: int = 1

    def dispatch(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: dict[str, Any],
    ) -> HttpResponse:
        """Check if the user is authenticated before dispatching the request."""
        if not request.user.is_authenticated:
            msg = "You must be logged in to view this page."
            raise Http404(msg)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict:
        """Return the context data for the template."""
        return super().get_context_data(**kwargs)

    def get_queryset(self) -> QuerySet[NutrientTracker]:
        """Return a queryset of nutrient trackers for the current user."""
        return (
            NutrientTracker.objects.all()
            .filter(user=self.request.user)
            .order_by("-date")
        )
