# Generated by Django 2.1.7 on 2019-03-29 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
