from django.views.generic import ListView
from apps.tracker_data.models import NutrientTracker
from django.shortcuts import render
from rest_framework import generics

# Create your views here.


# limit who can see the nutrient tracker
class NutrientTrackerListView(generics.ListAPIView):
    model = NutrientTracker
    template_name = "nutrient_tracker_list.html"
    context_object_name = "nutrient_trackers"
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return (
            NutrientTracker.objects.all()
            .filter(user=self.request.user)
            .order_by("-date")
        )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
