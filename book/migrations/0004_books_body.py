# Generated by Django 5.1.1 on 2024-10-28 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_books_total_rental'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
