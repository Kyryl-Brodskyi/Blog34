# Generated by Django 5.0.3 on 2024-04-06 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_alter_photo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='name',
            field=models.CharField(default='Default Name', max_length=255),
        ),
    ]
