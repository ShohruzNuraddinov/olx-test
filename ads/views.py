from django.shortcuts import render
from rest_framework import generics
from ads.serializers import AdsSerializer
from ads.models import Ads


# Create your views here.
class AdsListView(generics.ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
