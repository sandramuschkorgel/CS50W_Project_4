# Generated by Django 3.1.1 on 2020-11-11 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_posting'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='default_slug', editable=False),
        ),
    ]
