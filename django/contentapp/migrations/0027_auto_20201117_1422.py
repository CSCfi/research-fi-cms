# Generated by Django 3.1 on 2020-11-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0026_remove_singlefigure_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlefigure',
            name='placement_id',
            field=models.PositiveIntegerField(db_index=True, editable=False),
        ),
    ]
