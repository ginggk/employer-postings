# Generated by Django 2.1.7 on 2019-03-26 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_id',
            new_name='post_comment',
        ),
    ]