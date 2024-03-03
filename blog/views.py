from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BlogPost


def blog(request):
    items = BlogPost.objects.all()
    return render(request, 'archive.html', {"BlogPost":items})

