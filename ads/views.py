from django.shortcuts import render
from rest_framework import generics
from ads.serializers import AdsSerializer, CategorySerializer, FilterCategorySerializer
from ads.models import Ads, Category, SubCategory
from attribute.models import Attribute

from django.db.models import Prefetch


# Create your views here.
class AdsListView(generics.ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class MainCategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FilterCategoryListView(generics.ListAPIView):
    queryset = Category.objects.all().prefetch_related(
        Prefetch(
            "subcategory",
            queryset=SubCategory.objects.all().prefetch_related(
                Prefetch(
                    "attributes",
                    queryset=Attribute.objects.filter(is_filter=True),
                )
            ),
        )
    )
    serializer_class = FilterCategorySerializer
