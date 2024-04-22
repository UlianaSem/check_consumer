from rest_framework import generics

from main import models, serializers


class PlaceListAPIView(generics.ListAPIView):
    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceListSerializer


class PlaceRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Place.objects.all()
    serializer_class = serializers.PlaceSerializer
