# Generated by Django 2.1.1 on 2018-10-08 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Logger', '0004_record_trace'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='trace',
        ),
    ]
