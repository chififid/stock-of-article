# Generated by Django 3.0.6 on 2020-05-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_auto_20200516_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(null=True, upload_to='media/avatars'),
        ),
    ]