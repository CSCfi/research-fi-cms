# Generated by Django 3.1 on 2020-11-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0017_remove_shortcut_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='singlefigure',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False, verbose_name='order'),
            preserve_default=False,
        ),
    ]
