# Generated by Django 4.1.5 on 2023-01-24 21:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_tag_remove_picture_tags_picture_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Picture',
            new_name='Image',
        ),
    ]
