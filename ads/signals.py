from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from ads.models import Ads, Category, SubCategory


# @receiver(pre_save, sender=Ads)
# def update_detail(sender, instance, *args, **kwargs):
#     instance.address = instance.get_address_text()


# @receiver(post_save, sender=Ads)
# def create_ads(sender, instance, created, *args, **kwargs):
#     if created:
#         instance.save()


# @receiver(pre_save, sender=Ads)
# def update_adscount(sender, instance, created, *args, **kwargs):
#     if created:
#         instance.sub_category.category.ads_count += 1
#         instance.sub_category.ads_count += 1
#         instance.sub_category.save()
#         instance.sub_category.category.save()
