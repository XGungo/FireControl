# Generated by Django 3.2.5 on 2022-04-19 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vessel', '0005_rename_vessil_vessel'),
    ]

    operations = [
        migrations.AddField(
            model_name='vessel',
            name='type_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vessel',
            name='typename',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vessel',
            name='default_fires',
            field=models.ManyToManyField(default=0, to='Vessel.Missile'),
        ),
        migrations.AlterUniqueTogether(
            name='vessel',
            unique_together={('typename', 'type_id')},
        ),
        migrations.RemoveField(
            model_name='vessel',
            name='type',
        ),
    ]