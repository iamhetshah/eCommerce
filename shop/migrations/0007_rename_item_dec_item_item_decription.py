# Generated by Django 3.2 on 2021-04-19 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_img_name_item_item_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_dec',
            new_name='item_decription',
        ),
    ]
