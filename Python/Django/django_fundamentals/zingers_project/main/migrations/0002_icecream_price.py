# Generated by Django 2.2 on 2021-08-16 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]