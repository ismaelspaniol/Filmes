# Generated by Django 2.1.7 on 2019-03-21 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ferias', '0005_auto_20190321_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ferias',
            name='salary',
        ),
    ]
