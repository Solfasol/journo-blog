# Generated by Django 3.0.4 on 2020-05-24 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_auto_20200524_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='body',
        ),
    ]
