from django.views.generic import DetailView, ListView

from creator.models import Creator


class CreatorListView(ListView):
    model = Creator


class CreatorDetailView(DetailView):
    model = Creator
