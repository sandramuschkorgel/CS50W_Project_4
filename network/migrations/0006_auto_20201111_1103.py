# Generated by Django 3.1.1 on 2020-11-11 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20201111_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
