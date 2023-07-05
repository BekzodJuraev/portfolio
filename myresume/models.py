from django.db import models
from django.utils import timezone
# Create your models here.




class Photo(models.Model):
    upload = models.ImageField(verbose_name='Фото')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата Публикации')
    title=models.CharField(max_length=250,null=True)
    class Meta:
        ordering=['created']


class About(models.Model):
    title=models.CharField(max_length=250)
    username=models.CharField(max_length=250,default='Sometging')
    surname=models.CharField(max_length=250,default="Beka")
    text=models.TextField()
    skill_text=models.TextField(default="")
    created=models.DateTimeField(auto_now_add=True,null=True,verbose_name='Дата Публикации')

    class Meta:
        ordering=['created']




    def __str__(self):
        return self.title

class Adress(models.Model):
    adress=models.CharField(max_length=250)
    email=models.EmailField(blank=True)
    site_link=models.URLField(max_length=128)
    created=models.DateTimeField(auto_now_add=True,null=True,verbose_name='Дата Публикации')

    class Meta:
        ordering=['created']

class Skills(models.Model):
    skills=models.CharField(max_length=250)
    skills_level=models.CharField(max_length=250)

class Education(models.Model):
    Degree=models.CharField(max_length=250)
    univer_name=models.CharField(max_length=250)
    date_graduation=models.CharField(max_length=250)


class Languages(models.Model):
    language=models.CharField(max_length=200)
    level=models.CharField(max_length=200)


class Work(models.Model):
    title=models.CharField(max_length=200)
    company_name=models.CharField(max_length=200)
    duration=models.CharField(max_length=200)
    description=models.TextField()
    link_company=models.URLField(max_length=128)


class Projects(models.Model):
    project_name=models.CharField(max_length=200)
    description_projects=models.TextField()
    link_projects=models.URLField(max_length=128)

class Music(models.Model):
    music_name=models.CharField(max_length=200)


class Download(models.Model):
    file=models.FileField(upload_to='')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата Публикации')


    class Meta:
        ordering=['created']