# Generated by Django 4.1 on 2022-08-27 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_meetingmember_alter_meeting_channel'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='meetingmember',
            unique_together={('name', 'uid', 'channel')},
        ),
    ]
