# Generated by Django 5.0.3 on 2024-03-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_postphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='postphoto',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
    ]