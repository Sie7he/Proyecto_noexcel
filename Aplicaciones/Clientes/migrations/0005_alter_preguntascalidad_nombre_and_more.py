# Generated by Django 4.1.1 on 2022-09-09 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0004_preguntascalidad_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntascalidad',
            name='nombre',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='preguntascalidad',
            name='ticket',
            field=models.IntegerField(default=1),
        ),
    ]
