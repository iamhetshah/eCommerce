# Generated by Django 3.2 on 2021-04-20 12:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_item_u_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.AlterField(
            model_name='item',
            name='u_id',
            field=models.UUIDField(default=uuid.UUID('4c4d8dab-7d92-4887-87c5-320524c251ea'), editable=False, primary_key=True, serialize=False),
        ),
    ]
