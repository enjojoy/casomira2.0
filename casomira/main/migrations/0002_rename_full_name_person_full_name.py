# Generated by Django 4.1.3 on 2022-11-03 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='full_naMe',
            new_name='full_name',
        ),
    ]
