# Generated by Django 5.0.7 on 2024-08-28 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0045_orderdetails_paymentmethod"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderdetails",
            name="status",
            field=models.CharField(
                choices=[
                    ("delivered", "Delivered"),
                    ("inprogress", "In Progress"),
                    ("incomplete", "Incomplete"),
                ],
                max_length=20,
            ),
        ),
    ]