# Generated by Django 2.0.7 on 2018-07-05 17:26

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_auto_20170506_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=django_countries.fields.CountryField(default='Turkey', max_length=2),
        ),
    ]
