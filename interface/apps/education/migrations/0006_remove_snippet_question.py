# Generated by Django 3.2.17 on 2023-05-14 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_alter_topic_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='question',
        ),
    ]
