# Generated by Django 5.0.4 on 2024-05-31 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0015_alter_autores_libros'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autores',
            name='nacimiento',
        ),
    ]
