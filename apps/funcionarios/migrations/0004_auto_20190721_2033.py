# Generated by Django 2.2.3 on 2019-07-21 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_auto_20190707_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='empresas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa'),
        ),
    ]
