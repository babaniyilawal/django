from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render (request, 'itreporting/home.html')


def about(request):
    return render (request, 'itreporting/about.html')
    #return HttpResponse('<h1> Student IT Services - About U/h1>')

def contact(request):
    return render (request, 'itreporting/contact.html')
    #return HttpResponse('<h1> Student IT Services - Contact Us </h1>')
