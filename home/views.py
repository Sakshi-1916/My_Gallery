from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import gallery

def home(request):
  items = gallery.objects.all()
  return render(request, 'index.html', {"gallery":items})

