# Generated by Django 3.0.4 on 2020-05-23 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_auto_20200523_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='content_ptr',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]