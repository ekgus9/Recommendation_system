# Generated by Django 3.2.5 on 2022-02-15 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20220215_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='title_data',
            old_name='url_photo',
            new_name='photo_url',
        ),
    ]
