# Generated by Django 4.0 on 2023-11-20 07:32

from django.db import migrations
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0009_ads_address_set'),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name='ads',
            name='address_set',
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='ads',
            trigger=pgtrigger.compiler.Trigger(name='address_set', sql=pgtrigger.compiler.UpsertTriggerSql(func="\n                NEW.address = (SELECT CONCAT(common_region.title, ', ', common_district.title) FROM common_district JOIN common_region ON common_district.region_id=common_region.id WHERE common_district.id=NEW.district_id);RETURN NEW; \n\n           \n            ", hash='75e9cd47ba3b528fa9517aab00f6f3d2f940676a', operation='UPDATE OR INSERT', pgid='pgtrigger_address_set_65888', table='ads_ads', when='BEFORE')),
        ),
    ]
