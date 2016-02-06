from django.shortcuts import render
from home.models import Project

def index(request):
    return render(request, 'home/index.html')

def about_me(request):
    return render(request, 'home/about_me.html', {'sizes': ['100', '150', '200']})

def resume(request):
    return render(request, 'home/resume.html')

def projects(request):
    project_list = Project.objects.all()
    return render(request, 'home/projects.html', {'projects': project_list})
