# Generated by Django 4.2.6 on 2023-10-26 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0001_initial'),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdsAttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ads',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='attributes',
            field=models.ManyToManyField(blank=True, to='attribute.attribute'),
        ),
        migrations.CreateModel(
            name='AdsAttributeValueOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ads_attribute_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.adsattributevalue')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.attributeoption')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='adsattributevalue',
            name='ads',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.ads'),
        ),
        migrations.AddField(
            model_name='adsattributevalue',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attribute.attribute'),
        ),
    ]