# Generated by Django 4.0.4 on 2022-05-07 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_name',
        ),
        migrations.AddField(
            model_name='post',
            name='image_field',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
