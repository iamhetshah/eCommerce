# Generated by Django 3.2 on 2021-04-19 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_item_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_price_currency',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
