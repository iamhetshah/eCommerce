# Generated by Django 3.2 on 2021-04-19 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_item_item_price_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img_name',
            field=models.ImageField(upload_to=''),
        ),
    ]
