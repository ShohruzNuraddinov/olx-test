from django.db import models
from utils.models import BaseModel


# Create your models here.
class Attribute(BaseModel):
    class AttributeType(models.TextChoices):
        INTEGER = "integer"  # faqat son kiritiladi
        BUTTON = "button"  # button select
        SELECT = "select"  # ikkitalik tanlov
        MULTISELECT = "multiselect"  # selectli ko'p tanlov

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="category_attributes/", null=True, blank=True)
    type = models.CharField(
        max_length=255, choices=AttributeType.choices, default=AttributeType.INTEGER
    )

    is_required = models.BooleanField(default=False)
    is_list = models.BooleanField(default=False)

    order = models.IntegerField(default=0)

    class Meta:
        ordering = ("order",)


class AttributeOption(BaseModel):
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name="options"
    )

    title = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ("order",)
