# Generated by Django 4.0.4 on 2022-05-09 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contatos', '0009_alter_contato_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='create_data',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='update_data',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='create_data',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='update_data',
            field=models.DateField(auto_now=True),
        ),
    ]
