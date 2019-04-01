# Generated by Django 2.1.7 on 2019-03-29 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.TextField()),
                ('job_title', models.TextField()),
                ('location', models.TextField()),
                ('job_function', models.TextField()),
                ('employment_type', models.TextField()),
                ('company_industry', models.TextField()),
                ('seniority_level', models.TextField()),
                ('job_description', models.TextField()),
                ('logo', models.URLField()),
                ('date', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Posting'),
        ),
    ]
