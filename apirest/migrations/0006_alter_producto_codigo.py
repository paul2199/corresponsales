# Generated by Django 4.1.7 on 2023-03-03 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0005_alter_cliente_cedula_alter_cliente_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.TextField(),
        ),
    ]