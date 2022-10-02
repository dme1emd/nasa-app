# Generated by Django 3.2.6 on 2022-09-30 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('difficulty', models.PositiveSmallIntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)])),
                ('pic', models.ImageField(upload_to='question_pics')),
                ('right_answer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.answer')),
                ('wrong_answer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='quest', to='quiz.answer')),
            ],
        ),
    ]