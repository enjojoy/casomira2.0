# Generated by Django 4.1.3 on 2022-12-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_flight_landing_alter_flight_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='landing',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='landing'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='takeoff',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='takeoff'),
        ),
    ]
