# Generated by Django 4.1.3 on 2022-11-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='pics', upload_to='gallery'),
            preserve_default=False,
        ),
    ]