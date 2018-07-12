# Generated by Django 2.0.7 on 2018-07-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoneyRelations', '0006_auto_20180711_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='PaymentStatus',
            field=models.BooleanField(choices=[('Paid', 'Yes'), ('Not Paid', 'No')], default=True, verbose_name='Payment Status'),
        ),
    ]
