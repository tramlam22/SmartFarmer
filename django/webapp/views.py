from django.http import HttpResponse
from django.shortcuts import render
from .models import Testtemp
#or from .models import (name of class)

# Create your views here.
def home_view(request, *args, **kwargs):
  print(args,kwargs)
  print(request.user)
  return render(request,"index.html",{})

def about_view(request, *args, **kwargs):
  print(args,kwargs)
  print(request.user)
  return render(request,"About.html")

def graphs_view(request, *args, **kwargs):
  print(args,kwargs)
  print(request.user)

  obj = Testtemp.objects.values('temp')
  my_context = {
      #temp':obj.temp''
      #'db': "this is a string"
      'object': obj,
  }
  return render(request,"Graphs.html",my_context)

def contact_view(request, *args, **kwargs):
  print(args,kwargs)
  print(request.user)
  return render(request,"Contact.html",{})
