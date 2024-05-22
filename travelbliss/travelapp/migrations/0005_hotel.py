# Generated by Django 5.0.3 on 2024-04-01 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_alter_packagedetail_place_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('hotel_description', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(null=True, upload_to='image')),
                ('rating', models.FloatField(blank=True, null=True)),
                ('package_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.packages')),
            ],
        ),
    ]
