# Generated by Django 5.0.3 on 2024-03-30 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_post_alter_photo_description_alter_photo_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.post'),
        ),
    ]
