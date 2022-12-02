# Generated by Django 4.1.3 on 2022-11-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_activepeople_people_aircraft_aktivni_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aircraft',
            old_name='aktivni',
            new_name='active',
        ),
        migrations.AddField(
            model_name='person',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
