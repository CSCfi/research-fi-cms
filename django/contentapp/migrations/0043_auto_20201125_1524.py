# Generated by Django 3.1 on 2020-11-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0042_auto_20201125_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlefigure',
            name='placement_id',
            field=models.PositiveIntegerField(db_index=True, unique=True),
        ),
    ]
