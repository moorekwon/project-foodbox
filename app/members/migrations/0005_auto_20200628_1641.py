# Generated by Django 3.0.6 on 2020-06-28 07:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20200628_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duration',
            name='duration',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(regex='^[0-9\\d]{4}$')]),
        ),
    ]
