# Generated by Django 2.2.7 on 2019-12-01 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buraco', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buraco',
            old_name='user',
            new_name='cidadao',
        ),
    ]
