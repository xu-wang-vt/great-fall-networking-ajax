# Generated by Django 3.2.9 on 2021-11-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
