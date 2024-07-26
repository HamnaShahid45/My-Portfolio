from django.shortcuts import render, redirect
from .models import Header, Education, Skill, Experience, Project, Contact
from django.core.mail import EmailMessage


def home(request):
    return render(request, 'base.html')


def header_detail(request):
    headers = Header.objects.all()
    context = {
        'headers': headers
    }
    return render(request, 'header.html', context)


def education_list(request):
    education_items = Education.objects.all()
    context = {
        'education_items': education_items
    }
    return render(request, 'education.html', context)


def skill_list(request):
    skills = Skill.objects.all()
    context = {
        'skills': skills
    }
    return render(request, 'skills.html', context)


def experience_list(request):
    experiences = Experience.objects.all()
    context = {
        'experiences': experiences
    }
    return render(request, 'experience.html', context)


def project_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        us = Contact.objects.create(name=name, email=email, message=message)
        try:
            us.save()
            em = EmailMessage('Contact', [message], 'f2021266494@umt.edu.com', [email])
            em.send()
            return redirect('/')
        except:
            return render(request, 'contact.html', {'mes': 'Error'})
    return render(request, 'contact.html')
