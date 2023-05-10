# Generated by Django 4.2.1 on 2023-05-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('size', models.CharField(blank=True, max_length=30, null=True)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.CharField(blank=True, max_length=30, null=True)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
