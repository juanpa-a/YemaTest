# Generated by Django 2.2 on 2020-10-14 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201013_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='comments',
            field=models.TextField(default='no comments'),
            preserve_default=False,
        ),
    ]
