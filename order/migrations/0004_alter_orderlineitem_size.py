# Generated by Django 4.2.3 on 2023-07-24 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_orderlineitem_milk_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='size',
            field=models.CharField(blank=True, default='Standard', max_length=10, null=True),
        ),
    ]
