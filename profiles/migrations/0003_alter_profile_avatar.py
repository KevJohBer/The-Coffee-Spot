# Generated by Django 4.2.3 on 2023-08-07 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_default_address_profile_default_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='static/images/coffee-cup.png', null=True, upload_to='static/images'),
        ),
    ]