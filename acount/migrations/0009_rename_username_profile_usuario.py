# Generated by Django 4.1.7 on 2023-06-18 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acount', '0008_alter_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='usuario',
        ),
    ]
