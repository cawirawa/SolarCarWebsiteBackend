# Generated by Django 3.0.3 on 2020-02-24 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200223_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourteam',
            name='bio2',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
    ]
