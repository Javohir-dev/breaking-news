# Generated by Django 4.0 on 2023-06-04 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_occupation_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=300),
        ),
    ]
