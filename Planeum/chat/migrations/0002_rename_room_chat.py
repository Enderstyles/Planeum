# Generated by Django 4.0.3 on 2022-03-16 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room',
            new_name='Chat',
        ),
    ]
