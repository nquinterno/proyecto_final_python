# Generated by Django 4.1.7 on 2023-06-24 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acount', '0009_rename_username_profile_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='apellido',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='profile',
            name='descripcion',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nombre',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='profile',
            name='web',
            field=models.URLField(default=''),
        ),
    ]