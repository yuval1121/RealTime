# Generated by Django 2.2.17 on 2020-12-31 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20210101_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_people_inside',
            field=models.IntegerField(default=0),
        ),
    ]