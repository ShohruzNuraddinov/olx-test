from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.contrib.auth.views import LoginView
from django.db.models import Prefetch, Case, When, Value
from django.db import models
from django.utils.translation import get_language

from rest_framework.permissions import AllowAny
# from .forms import AuthForm


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


# Create your views here.


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AdsListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

    def get_queryset(self):
        print(get_language())
        return self.queryset.filter(language=get_language())


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


# class customLoginView(LoginView):
#     form_class = AuthForm
