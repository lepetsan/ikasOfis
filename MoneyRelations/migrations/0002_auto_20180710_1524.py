# Generated by Django 2.0.7 on 2018-07-10 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MoneyRelations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='MainCategory',
        ),
        migrations.AddField(
            model_name='expense',
            name='MainCategory',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to='MoneyRelations.MainCat'),
        ),
        migrations.RemoveField(
            model_name='expense',
            name='SubCategory',
        ),
        migrations.AddField(
            model_name='expense',
            name='SubCategory',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to='MoneyRelations.SubCat'),
        ),
    ]
