# Generated by Django 5.0 on 2023-12-12 01:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="last_price",
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
