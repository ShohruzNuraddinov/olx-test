# Generated by Django 4.2.6 on 2023-10-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_adsattributevalue_ads_content_subcategory_attributes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsattributevalue',
            name='value',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]