# Generated by Django 3.2.9 on 2021-11-22 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211122_2357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postbody',
            old_name='post_id',
            new_name='post',
        ),
    ]
