# Generated by Django 5.0.6 on 2024-05-21 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
