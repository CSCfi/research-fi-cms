# Generated by Django 3.1 on 2020-10-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0014_auto_20201029_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortcut',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
