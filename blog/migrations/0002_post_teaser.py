# Generated by Django 2.2.13 on 2020-06-16 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='teaser',
            field=models.TextField(blank=True),
        ),
    ]
