# Generated by Django 2.1.7 on 2019-03-14 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_person_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_doc', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='doc',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='clientes.Documento'),
        ),
    ]
