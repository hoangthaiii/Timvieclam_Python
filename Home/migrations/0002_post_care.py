# Generated by Django 3.1.5 on 2021-04-04 05:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='care',
            field=models.ManyToManyField(related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
