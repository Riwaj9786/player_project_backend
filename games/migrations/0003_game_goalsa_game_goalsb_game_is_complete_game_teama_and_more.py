# Generated by Django 5.1.5 on 2025-01-27 04:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_remove_player_preferred_position_delete_position'),
        ('games', '0002_alter_game_available_players_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='goalsA',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='game',
            name='goalsB',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='game',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='teamA',
            field=models.ManyToManyField(blank=True, null=True, related_name='teamA', to='accounts.player'),
        ),
        migrations.AddField(
            model_name='game',
            name='teamB',
            field=models.ManyToManyField(blank=True, null=True, related_name='teamB', to='accounts.player'),
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
