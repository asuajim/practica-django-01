# Generated by Django 2.1.4 on 2019-01-02 19:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190102_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 2, 19, 4, 11, 75345, tzinfo=utc), verbose_name='Fecha publicación'),
        ),
    ]