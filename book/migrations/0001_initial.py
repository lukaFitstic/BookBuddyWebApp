# Generated by Django 5.0.4 on 2024-04-28 12:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cognome', models.CharField(max_length=100)),
                ('eta', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genere', models.CharField(choices=[('Giallo', 'Giallo'), ('Cucina', 'Cucina'), ('Religioso', 'Religioso'), ('Azione', 'Azione'), ('Commedia', 'Commedia')], max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField(default='2024')),
                ('pages', models.IntegerField(default='0')),
                ('body', models.TextField(default='No body available')),
                ('slug', models.SlugField(default='')),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.autore')),
            ],
        ),
        migrations.CreateModel(
            name='ToRead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=False)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.book')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
