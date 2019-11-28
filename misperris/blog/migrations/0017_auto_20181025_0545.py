# Generated by Django 2.1.2 on 2018-10-25 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20181025_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo_vivienda',
            field=models.CharField(choices=[('PATIO_GRANDE', 'Casa con patio grande'), ('PATIO_PEQUEÑO', 'Casa con patio pequeño'), ('SIN_PATIO', 'Casa sin patio'), ('DEPTO', 'Departamento')], default='RESCATADO', max_length=30),
        ),
    ]