# Generated by Django 4.2.3 on 2023-08-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_to_go'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
