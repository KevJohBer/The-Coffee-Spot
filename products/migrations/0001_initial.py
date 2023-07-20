# Generated by Django 4.2.3 on 2023-07-19 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Product', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('category', models.CharField(blank=True, max_length=30, null=True)),
                ('category_id', models.IntegerField(default=0)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
    ]