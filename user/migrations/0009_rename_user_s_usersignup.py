# Generated by Django 5.0.1 on 2024-03-10 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_user_s'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_s',
            new_name='UserSignup',
        ),
    ]
