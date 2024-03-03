from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def about(request):
  template = loader.get_template('single.html')
  return HttpResponse(template.render())
