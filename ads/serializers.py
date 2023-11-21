from rest_framework import serializers
from ads import models
from common.serializers import DistrictSerializer
from attribute.serializers import (
    AttributeOptionSerializer,
    AttributeSerializer,
    FilterAttributeSerializer,
)

from attribute.models import Attribute, AttributeOption


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("id", "title", "ads_count", "image")


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.SubCategory
        fields = (
            "id",
            "title",
            "category",
            "ads_count",
        )


class FilterSubCategorySerializer(serializers.ModelSerializer):
    attributes = FilterAttributeSerializer(many=True)

    class Meta:
        model = models.SubCategory
        fields = ("id", "title", "ads_count", "attributes")


class FilterCategorySerializer(serializers.ModelSerializer):
    subcategory = FilterSubCategorySerializer(many=True)

    class Meta:
        model = models.Category
        fields = ("id", "title", "ads_count", "image", "subcategory")


class AdsAttributeValueOption(serializers.ModelSerializer):
    option = AttributeOptionSerializer()

    class Meta:
        model = models.AdsAttributeValueOption
        fields = (
            "id",
            "option",
        )


class AdsAttributeValueOptionCreateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.AdsAttributeValueOption
        fields = '__all__'


class AdsAttributeValueSerializer(serializers.ModelSerializer):
    value_options = AdsAttributeValueOption(many=True)
    attribute = AttributeSerializer()

    class Meta:
        model = models.AdsAttributeValue
        fields = ("id", "attribute", "value_options", "value")


class AdsAttributeValueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdsAttributeValue
        fields = ['id', 'attribute', 'ads', 'value']


class AdsSerializer(serializers.ModelSerializer):
    # sub_category = SubCategorySerializer()
    # district = DistrictSerializer()
    attribute_values = AdsAttributeValueSerializer(many=True)

    class Meta:
        model = models.Ads
        fields = (
            "id",
            "title",
            "image",
            "price",
            "is_top",
            # "sub_category",
            "address",
            "attribute_values",
            "created_at",
            "updated_at",
        )


class AdsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ads
        fields = [
            'id',
            'title',
            'image',
            'content',
            'price',
            'district',
            'is_top',
            'is_vip',
            'address',
            'sub_category',
            'created_at',
            'updated_at',
        ]


class VipAdsSerailizer(serializers.ModelSerializer):
    class Meta:
        mdoel = models.Ads
        fields = [
            'id',
            'title',
            'is_vip',
            'is_top',
            'image',
        ]


class FilterAttributeValueSerailizer(serializers.ModelSerializer):
    attribute = AttributeSerializer(many=False)
    ads = AdsSerializer()

    class Meta:
        model = models.AdsAttributeValue
        fields = [
            'id',
            'value',
            'attribute',
            'ads',
        ]
