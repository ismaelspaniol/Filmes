# Generated by Django 2.1.7 on 2019-03-14 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20190314_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='dependentes',
            new_name='depend',
        ),
    ]
