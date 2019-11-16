from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Testtemp
from . import plots
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
  '''
  def graphs_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)

    #obj = Testtemp.objects.values('temp')
    my_context = {
        #temp':obj.temp''
        #'db': "this is a string"
        #'object': obj,
        'object' : plots.get_graph()
    }
    return render(request,"Graphs.html",my_context)
'''
def contact_view(request, *args, **kwargs):
  print(args,kwargs)
  print(request.user)
  return render(request,"Contact.html",{})

class SimpleGraphs(TemplateView):
  template_name='Graphs.html'
  def get_context_data(self,**kwargs):
    context = super(SimpleGraphs, self).get_context_data(**kwargs)
    context['object'] = plots.get_graph()
    return context
    
def signin_view(request, *args, **kwargs):
  print(args,kwargs)
  print(request.user)
  return render(request, "Signin.html",{})

def create_account_view(request, *args, **kwargs):
  print(args, kwargs)
  print(request.user)
  return render(request, "CreateAccount.html", {})
