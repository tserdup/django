# Generated by Django 2.2 on 2019-05-20 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=50)),
                ('Area', models.CharField(max_length=30)),
                ('yourproperty', models.CharField(choices=[('house', 'House'), ('apartment', 'Apartment'), ('room', 'Room'), ('hostel', 'Hostel')], max_length=15)),
                ('img', models.ImageField(upload_to='image')),
                ('room', models.IntegerField()),
                ('garden', models.BooleanField()),
                ('water', models.IntegerField()),
            ],
        ),
    ]