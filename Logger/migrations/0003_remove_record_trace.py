# Generated by Django 2.1.1 on 2018-10-08 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Logger', '0002_auto_20181008_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='trace',
        ),
    ]