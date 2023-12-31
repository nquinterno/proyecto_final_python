# Generated by Django 4.1.7 on 2023-06-20 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acount', '0009_rename_username_profile_usuario'),
        ('web_ppal', '0002_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('texto', models.CharField(max_length=2500)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='media/posteos')),
                ('autor_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='acount.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
