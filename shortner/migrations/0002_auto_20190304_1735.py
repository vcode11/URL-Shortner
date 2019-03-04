# Generated by Django 2.1.7 on 2019-03-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='full_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.SlugField(max_length=6),
        ),
    ]
