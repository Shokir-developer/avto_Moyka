# Generated by Django 4.0.3 on 2022-05-04 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moyka', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mijoz',
            old_name='user',
            new_name='name',
        ),
    ]
