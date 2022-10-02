# Generated by Django 3.2.6 on 2022-10-01 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.PositiveSmallIntegerField(choices=[('really easy', 1), ('easy', 2), ('normal', 3), ('little hard', 4), ('hard', 5)]),
        ),
    ]