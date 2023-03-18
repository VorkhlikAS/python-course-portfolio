from django.urls import path
from creator.views import CreatorListView, CreatorDetailView

urlpatterns = [
    path("", CreatorListView.as_view(), name="creators"),
    path("<int:pk>/", CreatorDetailView.as_view(), name="creator"),
]
