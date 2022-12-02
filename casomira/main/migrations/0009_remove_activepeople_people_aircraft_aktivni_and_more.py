# Generated by Django 4.1.3 on 2022-11-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_activepeople_activeaircraft'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activepeople',
            name='people',
        ),
        migrations.AddField(
            model_name='aircraft',
            name='aktivni',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='ActiveAircraft',
        ),
        migrations.DeleteModel(
            name='ActivePeople',
        ),
    ]
