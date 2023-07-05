# Generated by Django 4.1.2 on 2023-07-05 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresume', '0008_alter_photo_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('description_projects', models.TextField()),
                ('link_projects', models.URLField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('link_company', models.URLField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='photo',
            name='upload',
            field=models.ImageField(upload_to='', verbose_name='Фото'),
        ),
    ]
