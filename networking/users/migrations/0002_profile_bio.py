# Generated by Django 3.0.8 on 2020-07-26 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='default bio', max_length=100),
            preserve_default=False,
        ),
    ]