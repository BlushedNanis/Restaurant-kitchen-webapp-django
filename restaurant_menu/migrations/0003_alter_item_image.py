# Generated by Django 5.0.6 on 2024-05-17 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_menu', '0002_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='uploads\\'),
        ),
    ]
