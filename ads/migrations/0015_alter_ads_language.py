# Generated by Django 3.2.23 on 2023-11-30 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0014_ads_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='language',
            field=models.CharField(choices=[('uz', 'Uzbek'), ('en', 'English'), ('ru', 'Russian')], max_length=10),
        ),
    ]
