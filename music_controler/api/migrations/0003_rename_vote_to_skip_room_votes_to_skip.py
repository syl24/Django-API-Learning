# Generated by Django 3.2 on 2021-05-24 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_room_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='vote_to_skip',
            new_name='votes_to_skip',
        ),
    ]
