import pgtrigger

from django.db import models
from utils.models import BaseModel
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.
User = get_user_model()


class languageChoice(models.Choices):
    uz = "UZ"
    en = "EN"
    ru = "RU"


class Category(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="main_category")

    ads_count = models.IntegerField(default=0)

    def ads_counter(self):
        return models.F('subcategory__sub_category__')

    class Meta:
        triggers = [
            pgtrigger.Trigger(
                name='ads_count_update',
                operation=pgtrigger.Delete | pgtrigger.Update | pgtrigger.Insert,
                when=pgtrigger.Before,
                func=f"""
                    NEW.ads_count = (
                            SELECT COUNT(*) FROM ads_ads
                        );
                    RETURN NEW; 
                """
            )
        ]


class SubCategory(BaseModel):
    title = models.CharField(max_length=255)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategory"
    )
    attributes = models.ManyToManyField("attribute.Attribute", blank=True)

    ads_count = models.IntegerField(default=0)


# class AdsImage(BaseModel):
#     ads = models.ForeignKey("ads.Ads", on_delete=models.CASCADE, related_name="images")


class Ads(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="ads_images", blank=True, null=True)
    price = models.IntegerField(default=0)
    content = models.TextField()

    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="sub_category"
    )
    district = models.ForeignKey("common.District", on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_top = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)

    language = models.CharField(
        max_length=10, choices=settings.LANGUAGES)

    # EXTRA FIELDS
    address = models.CharField(max_length=255, null=True, blank=True)

    def get_address_text(self):
        return f"{self.district.region.title}, {self.district.title}"

    class Meta:
        verbose_name_plural = "Ads"
        ordering = ('id',)

    # class Meta:
    #     triggers = [
    #         pgtrigger.Trigger(
    #             name='address_set',
    #             operation=pgtrigger.Update | pgtrigger.Insert,
    #             when=pgtrigger.Before,
    #             func=f"""
    #                 NEW.address = (SELECT CONCAT(common_region.title, ', ', common_district.title) FROM common_district JOIN common_region ON common_district.region_id=common_region.id WHERE common_district.id=NEW.district_id);RETURN NEW;
    #             """,
    #         ),
    #     ]


class AdsAttributeValue(BaseModel):
    value = models.CharField(max_length=255, null=True, blank=True)

    ads = models.ForeignKey(
        Ads, on_delete=models.CASCADE, related_name="attribute_values"
    )
    attribute = models.ForeignKey(
        "attribute.Attribute", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = 'Ads Attribute Value'


class AdsAttributeValueOption(BaseModel):
    ads_attribute_value = models.ForeignKey(
        AdsAttributeValue, on_delete=models.CASCADE, related_name="value_options"
    )
    option = models.ForeignKey(
        "attribute.AttributeOption", on_delete=models.CASCADE)
