# Generated by Django 3.0.3 on 2020-02-24 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20200223_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourteam',
            name='bio',
            field=models.TextField(max_length=500),
        ),
    ]
