# Generated by Django 5.1.5 on 2025-02-07 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_alter_playergamerating_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='teamnameA',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='teamnameB',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
