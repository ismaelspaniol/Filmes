# Generated by Django 2.1.7 on 2019-03-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferias', '0004_auto_20190321_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='ferias',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ferias',
            name='dias_com_deducao_faltas',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='ferias',
            name='dias_direito',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='ferias',
            name='dias_saldo',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='ferias',
            name='dias_saldo_v2',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='ferias',
            name='faltas_nao_justificadas',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
