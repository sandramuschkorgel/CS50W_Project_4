# Generated by Django 3.1.1 on 2020-11-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='default_slug', editable=False),
        ),
    ]
