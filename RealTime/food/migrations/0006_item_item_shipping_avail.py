# Generated by Django 2.2.17 on 2020-12-31 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_remove_item_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_shipping_avail',
            field=models.BooleanField(default=False),
        ),
    ]
