# Generated by Django 3.2.5 on 2022-06-02 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vessel', '0010_auto_20220601_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='missile',
            name='damage',
            field=models.FloatField(default=0.5),
        ),
    ]