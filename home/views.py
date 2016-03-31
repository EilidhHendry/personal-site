from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

from home.models import Project, Education, Job, PersonalInfo, Overview
from home.forms import ContactForm

def index(request):
    return render(request, 'home/index.html')

def about_me(request):
    return render(request, 'home/about_me.html', {'sizes': ['100', '150', '200']})

def resume(request):
    personal_info = PersonalInfo.objects.all()
    overview = Overview.objects.all()
    education = Education.objects.all()
    project_list = Project.objects.all()
    job_list = Job.objects.all()
    return render(request, 'home/resume.html', {
        'personal_info': personal_info,
        'overview': overview,
        'education': education,
        'project_list': project_list,
        'job_list': job_list
        })

def projects(request):
    project_list = Project.objects.all()
    return render(request, 'home/projects.html', {'projects': project_list})

