# Generated by Django 5.1.1 on 2024-10-12 20:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['-publish']},
        ),
        migrations.AddField(
            model_name='books',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
