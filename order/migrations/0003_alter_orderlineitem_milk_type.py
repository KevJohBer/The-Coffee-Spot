# Generated by Django 4.2.3 on 2023-07-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderlineitem_milk_type_orderlineitem_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='milk_type',
            field=models.CharField(blank=True, default='Milk', max_length=30, null=True),
        ),
    ]
