# Generated by Django 5.0.6 on 2024-06-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
