# Generated by Django 4.0.2 on 2022-02-10 02:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_alter_purchase_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 5, 11, 17, 221111)),
        ),
    ]
