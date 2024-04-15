# Generated by Django 4.2.11 on 2024-04-15 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_album_release_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='albums',
        ),
        migrations.AddField(
            model_name='list',
            name='albums',
            field=models.ManyToManyField(blank=True, to='app.album'),
        ),
    ]
