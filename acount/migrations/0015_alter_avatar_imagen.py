# Generated by Django 4.1.7 on 2023-06-27 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acount', '0014_alter_avatar_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
