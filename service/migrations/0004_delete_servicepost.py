# Generated by Django 5.0.2 on 2024-03-18 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_provider_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServicePost',
        ),
    ]