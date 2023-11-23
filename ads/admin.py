import csv
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import path

from imagekit.admin import AdminThumbnail

from .models import Ads, AdsAttributeValue, AdsAttributeValueOption
from .forms import CSVImortForm

# Register your models here.


class AdsAttrbuteOptionValueInline(admin.TabularInline):
    model = AdsAttributeValueOption
    extra = 1


class AdsAttributeValueInline(admin.TabularInline):
    model = AdsAttributeValue
    extra = 1
    inlines = [AdsAttrbuteOptionValueInline]


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_per_page = 10
    date_hierarchy = 'created_at'
    change_list_template = "entities/ads_changelist.html"

    # image_display = AdminThumbnail(image_field='image')
    # image_display.short_description = 'Image'
    readonly_fields = ['created_at', 'updated_at', 'image_get',]
    inlines = [AdsAttributeValueInline]
    list_display = [
        'id',
        'title',
        'price',
        # 'image_display',
        'sub_category',
        'is_vip',
        'is_top',
        'created_at',
        'updated_at',
    ]

    list_filter = [
        'id',
        'title',
        'price',
        'created_at',
        'updated_at',
    ]
    search_fields = [
        'title',
        'sub_category__category__title',
        'content'
    ]
    actions = ['export_as_csv',
               'mark_is_vip', 'mark_is_top',
               'mark_not_is_top', 'mark_not_is_vip',
               ]

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def mark_is_vip(self, request, queryset):
        queryset.update(is_vip=True)

    def mark_is_top(self, request, queryset):
        queryset.update(is_top=True)

    def mark_not_is_vip(self, request, queryset):
        queryset.update(is_vip=False)

    def mark_not_is_top(self, request, queryset):
        queryset.update(is_top=False)

    def image_get(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width/10,
            height=obj.image.height/10,
        ))

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                  for field in field_names])
        return response

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            reader = csv.reader(csv_file)
            # ...
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CSVImortForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )


@admin.register(AdsAttributeValue)
class AdsAttributeValueAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'ads',
        'value',
    ]
    list_filter = [
        'id',
        'ads',
        'value',
    ]
    search_fields = [
        'id',
        'ads__title',
        'value',
    ]
    inlines = [AdsAttrbuteOptionValueInline]


@admin.register(AdsAttributeValueOption)
class AdsAttributeValueOptionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'ads_attribute_value',
        'option',
    ]
    list_display = [
        'id',
        'ads_attribute_value',
        'option',
    ]
    search_fields = [
        'id',
        'ads_attribute_value',
        'option',
    ]
