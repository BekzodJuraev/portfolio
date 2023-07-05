from django.shortcuts import render

from .models import Photo,About,Adress,Skills,Education,Work,Music,Languages,Projects,Download


def about_view(request):
    abouts=About.objects.all().last()
    adress=Adress.objects.all().last()
    skills=Skills.objects.all()
    educations=Education.objects.all()
    photo=Photo.objects.all().last()
    languages=Languages.objects.all()
    musics=Music.objects.all()
    works=Work.objects.all()
    projects=Projects.objects.all()
    download=Download.objects.all().last()
    return render(request,'myresume/base.html',
                  {'abouts': abouts,
                   'adress':adress,
                   'skills':skills,
                   'educations':educations,
                   'photo':photo,
                   'languages':languages,
                   'musics':musics,
                   'works':works,
                   'projects':projects,
                   'download':download})



