from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

from home.models import Project
from home.forms import ContactForm

def index(request):
    return render(request, 'home/index.html')

def about_me(request):
    return render(request, 'home/about_me.html', {'sizes': ['100', '150', '200']})

def resume(request):
    return render(request, 'home/resume.html')

def projects(request):
    project_list = Project.objects.all()
    return render(request, 'home/projects.html', {'projects': project_list})

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name','')
            contact_email = request.POST.get('contact_email','')
            form_content = request.POST.get('content','')

            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
                })
            content = template.render(context)

            email = EmailMessage(
                    "New contact form submission",
                    content,
                    "Your website" + '',
                    ['youremail@gmail.com'],
                    headers = {'Reply-To': contact_email })
            email.send()
            return redirect('contact')
    return render(request, 'home/contact.html', {'form': form_class})
