# Generated by Django 4.1.1 on 2022-12-14 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historical', '0006_historical_fields_alter_historical_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historical',
            old_name='fields',
            new_name='post',
        ),
        migrations.AddField(
            model_name='historical',
            name='pre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
