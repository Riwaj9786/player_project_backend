# Generated by Django 5.1.5 on 2025-01-24 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_rename_position_player_preferred_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_player',
            field=models.CharField(blank=True, default='Cristiano Ronaldo', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_team',
            field=models.CharField(blank=True, default='Real Madrid', max_length=355, null=True),
        ),
    ]
