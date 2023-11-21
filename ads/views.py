from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


from ads.serializers import (
    AdsSerializer,
    CategorySerializer,
    FilterCategorySerializer,
    VipAdsSerailizer,
    AdsAttributeValueCreateSerializer,
    AdsAttributeValueOptionCreateSerailizer,
    AdsCreateSerializer
)
from ads.models import Ads, Category, SubCategory, AdsAttributeValue, AdsAttributeValueOption
from attribute.models import Attribute

from django.db.models import Prefetch, Case, When, Value
from django.db import models

# Create your views here.


class AdsListView(generics.ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class MainCategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filterset_fields = ['title']


class VipAdsListView(generics.ListAPIView):
    queryset = Ads.objects.filter(is_vip=True).order_by('?')
    serializer_class = VipAdsSerailizer


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

    # def get(self, request):
    # queryset = Category.objects.all().prefetch_related(
    #     Prefetch(
    #         'subcategory',
    #         queryset=SubCategory.objects.all().prefetch_related(
    #             'attributes',
    #             queryset=Attribute.objects.all().prefetch_related(
    #                 ''
    #             )
    #         )
    #     )
    # )
    # return


class FilterAdsListView(generics.ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

    filterset_fields = ['sub_category']


class AdsCreateView(generics.CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsCreateSerializer


class AttributeValueCreateView(generics.CreateAPIView):
    queryset = AdsAttributeValue.objects.all()
    serializer_class = AdsAttributeValueCreateSerializer


class AttributeOptionValueCreateView(generics.CreateAPIView):
    queryset = AdsAttributeValueOption.objects.all()
    serializer_class = AdsAttributeValueOptionCreateSerailizer
