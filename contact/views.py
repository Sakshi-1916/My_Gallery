from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import ContactFormEntry
from .forms import ContactForm 

def contact(request):
  #template = loader.get_template('contact.html')
  #return HttpResponse(template.render())
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      # Create a new model instance with form data
      entry = ContactFormEntry(
        name=form.cleaned_data['name'],
        email=form.cleaned_data['email'],
        message=form.cleaned_data['message'],
        )
      entry.save()
      return redirect('http://127.0.0.1:8000/home/')  # Redirect to success page after saving
  else:
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)
