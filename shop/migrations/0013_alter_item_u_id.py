# Generated by Django 3.2 on 2021-04-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20210420_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='u_id',
            field=models.CharField(max_length=100),
        ),
    ]
