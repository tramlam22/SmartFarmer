from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
  print(args,kwargs)
  print(request.user)
  return render(request,"index.html",{})

def about_view(request, *args, **kwargs):
  print(args,kwargs)
  print(request.user)
  return render(request,"About.html",{})

def graphs_view(request, *args, **kwargs):
  print(args,kwargs)
  print(request.user)
  return render(request,"Graphs.html",{})

def contact_view(request, *args, **kwargs):
  print(args,kwargs)
  print(request.user)
  return render(request,"Contact.html",{})
