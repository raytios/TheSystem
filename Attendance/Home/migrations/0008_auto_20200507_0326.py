# Generated by Django 3.0.6 on 2020-05-06 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0007_auto_20200506_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_choose',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
