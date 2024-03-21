# Generated by Django 5.0.2 on 2024-03-21 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_delete_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='currency_code',
            field=models.CharField(choices=[('cad', 'CAD'), ('usd', 'USD')], default='cad', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male', max_length=50),
        ),
    ]
