# Generated by Django 3.0.4 on 2020-04-04 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0004_auto_20200405_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='content',
            name='published_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='published by'),
        ),
    ]