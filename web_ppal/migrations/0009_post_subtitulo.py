# Generated by Django 4.1.7 on 2023-06-24 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_ppal', '0008_alter_mensaje_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitulo',
            field=models.CharField(default='', max_length=100),
        ),
    ]
