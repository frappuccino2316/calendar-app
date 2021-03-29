# Generated by Django 3.1.6 on 2021-03-29 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_auto_20210301_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationtoteam',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
