# Generated by Django 2.1.1 on 2018-10-09 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Logger', '0008_record_trace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trace',
            name='tag',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
