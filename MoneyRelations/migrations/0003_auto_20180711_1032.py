# Generated by Django 2.0.7 on 2018-07-11 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoneyRelations', '0002_auto_20180710_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='MainCategory',
            field=models.CharField(choices=[('Demirbaş', 'Demirbaş'), ('Yatırım', 'Yatırım'), ('Sabit Gider', 'Sabit Gider'), ('Pazarlama', 'Pazarlama')], default='', max_length=9, verbose_name='Main Category'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='SubCategory',
            field=models.CharField(choices=[('Bilgisayar', 'Bilgisayar'), ('Ticket', 'Ticket'), ('Ekip Yemek / Motivasyon', 'Ekip Yemek / Motivasyon'), ('IK', 'IK'), ('Diğer', 'Diğer'), ('POP', 'POP'), ('Ofis', 'Ofis'), ('Marka / Patent', 'Marka / Patent'), ('Internet', 'Internet'), ('Aidat / Isınma', 'Aidat / Isınma'), ('Vergi/Harç/Noter', 'Vergi/Harç/Noter')], default='', max_length=9, verbose_name='Sub Category'),
        ),
    ]