# Generated by Django 5.0.4 on 2024-04-20 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0002_autore_alter_book_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="genere",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
