# Generated by Django 2.2.24 on 2022-02-11 16:59

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0073_auto_20220128_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='providedtextasset',
            name='shared_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='providedtextassetconfiguration',
            name='shared_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
