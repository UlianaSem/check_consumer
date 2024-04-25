from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from main import models, serializers


class PlaceListAPIView(generics.ListAPIView):
    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceListSerializer
    permission_classes = [IsAuthenticated]


class PlaceRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer
    permission_classes = [IsAuthenticated]
