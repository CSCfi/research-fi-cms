# Generated by Django 3.1 on 2020-11-20 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0036_auto_20201120_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singlefigure',
            name='link_id',
        ),
    ]
