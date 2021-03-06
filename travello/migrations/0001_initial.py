# Generated by Django 3.0.5 on 2021-11-05 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('rooms', models.PositiveIntegerField(default=0)),
                ('description', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_image1', models.ImageField(default='photo', upload_to='room_images')),
                ('room_image2', models.ImageField(default='photo', upload_to='room_images')),
                ('room_image3', models.ImageField(default='photo', upload_to='room_images')),
                ('room_type', models.CharField(choices=[(1, 'Single'), (2, 'Double'), (3, 'Triple'), (4, 'Quad'), (5, 'Queen'), (6, 'King'), (7, 'Twin'), (8, 'Hollywood-Twin'), (9, 'Studio'), (10, 'Suite')], default=1, max_length=30)),
                ('room_price', models.PositiveIntegerField(default=300)),
                ('room_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travello.Cities')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_description', models.TextField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travello.Room_Type')),
            ],
        ),
    ]
