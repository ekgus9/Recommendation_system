# Generated by Django 3.2.5 on 2022-02-14 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20220214_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mainphoto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
