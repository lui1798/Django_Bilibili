# Generated by Django 2.0.6 on 2018-06-20 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='context',
            new_name='content',
        ),
    ]