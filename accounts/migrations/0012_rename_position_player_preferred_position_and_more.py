# Generated by Django 5.1.5 on 2025-01-24 09:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_invitedmanager_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='position',
            new_name='preferred_position',
        ),
        migrations.AlterField(
            model_name='invitedmanager',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('PLAYER', 'Player'), ('MANAGER', 'Manager')], default='PLAYER', max_length=25),
        ),
    ]
