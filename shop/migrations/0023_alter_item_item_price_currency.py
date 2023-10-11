# Generated by Django 3.2 on 2021-05-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_item_item_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_price_currency',
            field=models.CharField(choices=[('1', 'INR'), ('2', 'USD')], max_length=5),
        ),
    ]
