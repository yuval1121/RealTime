# Generated by Django 2.2.17 on 2021-01-01 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_auto_20210101_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_people_inside',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
