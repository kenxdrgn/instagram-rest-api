# Generated by Django 3.2.3 on 2021-05-18 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_post_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='currentName',
        ),
    ]