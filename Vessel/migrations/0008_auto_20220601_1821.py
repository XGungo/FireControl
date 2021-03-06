# Generated by Django 3.2.5 on 2022-06-01 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vessel', '0007_auto_20220601_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vessel',
            name='default_fires',
        ),
        migrations.AddField(
            model_name='vessel',
            name='default_fire1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='fire1', to='Vessel.missile'),
        ),
        migrations.AddField(
            model_name='vessel',
            name='default_fire2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='fire2', to='Vessel.missile'),
        ),
    ]
