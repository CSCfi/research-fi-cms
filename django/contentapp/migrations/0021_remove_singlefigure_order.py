# Generated by Django 3.1 on 2020-11-17 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0020_singlefigure_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singlefigure',
            name='order',
        ),
    ]
