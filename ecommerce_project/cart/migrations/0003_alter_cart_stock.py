# Generated by Django 5.1.6 on 2025-03-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_quantity_cart_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='stock',
            field=models.IntegerField(default=1),
        ),
    ]
