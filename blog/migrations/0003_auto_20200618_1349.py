# Generated by Django 2.2.13 on 2020-06-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_teaser'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='niveau',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='preparation_time',
            field=models.TextField(blank=True),
        ),
    ]
