# Generated by Django 4.1.7 on 2023-06-17 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acount', '0006_alter_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='username',
        ),
    ]