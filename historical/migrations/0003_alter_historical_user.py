# Generated by Django 4.1.1 on 2022-12-09 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('historical', '0002_alter_historical_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historical',
            name='user',
            field=models.ForeignKey(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
