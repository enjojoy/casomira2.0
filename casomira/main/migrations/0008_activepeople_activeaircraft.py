# Generated by Django 4.1.3 on 2022-11-03 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_delete_activeaircraft_delete_activeunits_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivePeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='person', to='main.person')),
            ],
        ),
        migrations.CreateModel(
            name='ActiveAircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aircrafts', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='aircraft', to='main.aircraft')),
            ],
        ),
    ]
