# Generated by Django 2.2 on 2019-05-21 07:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_room_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.IntegerField(),
        ),
    ]