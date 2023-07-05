# Generated by Django 4.1.2 on 2023-07-05 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresume', '0005_education_skills_alter_adress_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='adress',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='about',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата Публикации'),
        ),
        migrations.AddField(
            model_name='adress',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата Публикации'),
        ),
    ]