# Generated by Django 3.2.14 on 2022-07-14 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Qusestion',
            new_name='Question',
        ),
    ]
