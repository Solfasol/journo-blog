# Generated by Django 3.0.7 on 2020-07-03 12:54

from django.db import migrations, models
import django.db.models.deletion
import solfasol.issues.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(choices=[(2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], verbose_name='year')),
                ('month', models.PositiveSmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], verbose_name='month')),
                ('name', models.CharField(max_length=50, verbose_name='name / number')),
                ('pdf', models.FileField(blank=True, null=True, upload_to=solfasol.issues.models.issue_pdf_path, verbose_name='PDF')),
                ('cover', models.ImageField(blank=True, null=True, upload_to=solfasol.issues.models.issue_cover_image_path, verbose_name='cover')),
                ('page_count', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='page count')),
                ('tags', models.ManyToManyField(blank=True, to='tags.Tag', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'issue',
                'verbose_name_plural': 'issues',
                'ordering': ('-year', '-month'),
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='number')),
                ('image', models.ImageField(blank=True, null=True, upload_to=solfasol.issues.models.page_image_path, verbose_name='image')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.Issue', verbose_name='issue')),
                ('tags', models.ManyToManyField(blank=True, to='tags.Tag', verbose_name='tags')),
            ],
        ),
    ]
