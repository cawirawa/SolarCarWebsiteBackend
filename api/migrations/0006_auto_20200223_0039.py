# Generated by Django 3.0.3 on 2020-02-23 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200223_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourteam',
            name='profile_image',
            field=models.ImageField(blank=True, default='https://i.stack.imgur.com/l60Hf.png', max_length=255, null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
