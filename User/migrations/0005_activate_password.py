# Generated by Django 3.0.6 on 2020-05-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_activate'),
    ]

    operations = [
        migrations.AddField(
            model_name='activate',
            name='password',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]