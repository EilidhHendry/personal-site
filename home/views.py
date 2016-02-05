from django.shortcuts import render, render_to_response
from django.template import RequestContext
from home.models import Project

def index(request):
    return render_to_response('home/index.html')

def about_me(request):
    return render_to_response('home/about_me.html')

def resume(request):
    return render_to_response('home/resume.html')

def projects(request):
    project_list = Project.objects.all()
    return render(request, 'home/projects.html', {'projects': project_list})
