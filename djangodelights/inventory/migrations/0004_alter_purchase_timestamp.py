# Generated by Django 4.0.2 on 2022-02-09 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_purchase_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 9, 14, 6, 48, 981623)),
        ),
    ]
