from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'intro.html')

def skills(request):
    return render(request, 'skills.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')

def pybot(request):
    return render(request, 'pybot.html')