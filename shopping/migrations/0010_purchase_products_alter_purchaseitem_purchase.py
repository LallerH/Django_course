# Generated by Django 5.0.6 on 2024-07-01 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0009_alter_address_options_purchaseitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='products',
            field=models.ManyToManyField(through='shopping.PurchaseItem', to='shopping.product'),
        ),
        migrations.AlterField(
            model_name='purchaseitem',
            name='purchase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='shopping.purchase'),
        ),
    ]
