# Generated by Django 5.0.7 on 2024-08-18 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0014_remove_product_highgloss_remove_product_lowgloss_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="inventory",
        ),
    ]