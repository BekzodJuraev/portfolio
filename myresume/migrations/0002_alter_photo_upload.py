# Generated by Django 4.1.2 on 2023-06-19 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='upload',
            field=models.ImageField(upload_to='uploads/', verbose_name='Фото'),
        ),
    ]
