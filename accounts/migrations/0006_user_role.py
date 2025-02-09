# Generated by Django 5.1.5 on 2025-01-24 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('PLAYER', 'Player'), ('MANAGER', 'Manager')], null=True),
        ),
    ]
