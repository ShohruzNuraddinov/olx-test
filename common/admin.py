from django.contrib import admin

# Register your models here.
# django admin register all model
from django.apps import apps
from ads.models import Ads


models = apps.get_models()

for model in models:
    try:
        # if model
        admin.site.register(model)
    except:
        pass
