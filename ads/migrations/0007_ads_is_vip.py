# Generated by Django 4.2.6 on 2023-11-04 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_alter_ads_image_alter_subcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='is_vip',
            field=models.BooleanField(default=False),
        ),
    ]
