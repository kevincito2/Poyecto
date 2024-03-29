# Generated by Django 2.1.2 on 2018-10-09 03:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nombre_completo', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('region', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=30)),
                ('tipo_vivienda', models.CharField(max_length=25)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_publicacion', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
