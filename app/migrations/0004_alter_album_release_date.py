# Generated by Django 4.2.11 on 2024-04-15 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_list_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.CharField(max_length=30),
        ),
    ]
