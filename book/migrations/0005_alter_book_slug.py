# Generated by Django 5.0.3 on 2024-04-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=100)),
        ),
    ]
