# Generated by Django 3.1.1 on 2020-11-26 11:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_auto_20201126_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
