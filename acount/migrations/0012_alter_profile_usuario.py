# Generated by Django 4.1.7 on 2023-06-24 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acount', '0011_alter_profile_apellido_alter_profile_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]