# Generated by Django 3.2.5 on 2022-02-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_rename_url_photo_title_data_photo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='title_data',
            name='recommend',
            field=models.TextField(blank=True),
        ),
    ]
