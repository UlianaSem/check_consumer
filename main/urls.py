from main.apps import MainConfig
from django.urls import path

from main.views import PlaceListAPIView, PlaceRetrieveAPIView

app_name = MainConfig.name

urlpatterns = [
    path('places/', PlaceListAPIView.as_view(), name='get_places'),
    path('analytics/<int:pk>/', PlaceRetrieveAPIView.as_view(), name='get_analytics'),
]
