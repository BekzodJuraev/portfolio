from django.contrib import admin
from .models import Photo,About,Adress,Skills,Education,Work,Music,Languages,Projects,Download

# Register your models here.
@admin.register(Photo)
class Photo(admin.ModelAdmin):
    list_display = ['upload','created','title']


@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ['title','surname','username','created']


@admin.register(Adress)
class Adress(admin.ModelAdmin):
    list_display = ['adress','email','site_link','created'
    ]


@admin.register(Skills)
class Skills(admin.ModelAdmin):
    list_display = ['skills','skills_level']

@admin.register(Education)
class Education(admin.ModelAdmin):
    list_display = ['Degree','univer_name','date_graduation']

@admin.register(Languages)
class Languages(admin.ModelAdmin):
    list_display = ['language','level']

@admin.register(Music)
class Music(admin.ModelAdmin):
    list_display = ['music_name']
@admin.register(Work)
class Work(admin.ModelAdmin):
    list_display = ['title','company_name','duration',]

@admin.register(Projects)
class Projects(admin.ModelAdmin):
    list_display = ['project_name',]

@admin.register(Download)
class Projects(admin.ModelAdmin):
    list_display = ['file','created']