# Generated by Django 4.2.3 on 2023-08-07 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='static/images/coffee-cup.png', null=True, upload_to='static/images'),
        ),
    ]
