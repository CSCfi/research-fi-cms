# Generated by Django 3.1 on 2020-11-17 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0023_auto_20201117_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='singlefigure',
            options={'ordering': ('placement_id', 'figure')},
        ),
    ]
