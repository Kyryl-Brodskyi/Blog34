# Generated by Django 5.0.3 on 2024-03-29 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Posts_photos', verbose_name='Картинка')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Пост')),
            ],
        ),
    ]
