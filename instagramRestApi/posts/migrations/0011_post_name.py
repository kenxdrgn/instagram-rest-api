# Generated by Django 3.2.3 on 2021-05-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_rename_datatype_post_imagetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='', max_length=32),
        ),
    ]
