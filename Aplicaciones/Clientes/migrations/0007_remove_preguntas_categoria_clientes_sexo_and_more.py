# Generated by Django 4.1 on 2022-09-13 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0006_merge_20220910_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preguntas',
            name='categoria',
        ),
        migrations.AddField(
            model_name='clientes',
            name='sexo',
            field=models.CharField(default='masculino', max_length=10),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Preguntas',
        ),
    ]
