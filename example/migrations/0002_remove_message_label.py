# Generated by Django 2.2 on 2020-10-29 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='label',
        ),
    ]