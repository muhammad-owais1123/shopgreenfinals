# Generated by Django 5.0.7 on 2024-08-18 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0016_remove_productinfo_gloss_product_gloss"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=30),
        ),
    ]