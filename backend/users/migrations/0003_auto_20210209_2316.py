# Generated by Django 3.1.6 on 2021-02-09 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_team_of_affiliation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address'),
        ),
    ]