# Generated by Django 3.0.8 on 2020-10-15 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_titles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, to='api_titles.Genre', verbose_name='Жанр'),
        ),
    ]
