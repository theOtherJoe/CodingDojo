# Generated by Django 2.2 on 2021-08-20 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_order_total_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_cost',
        ),
    ]
