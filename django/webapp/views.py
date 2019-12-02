from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Testtemp, Account
from .import plots
from webapp.forms import *
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
    
class signin_view(TemplateView):
  template_name = 'Signin.html'

  def get(self,request):
    form = loginForm()
    return (render(request, self.template_name, {'form' : form}))

  def post(self,request):
    form = loginForm(request.POST)
    user = request.POST["username"]
    pwd = request.POST["password"]
    if not Account.objects.all().filter(username=user) or not Account.objects.all().filter(password=pwd):
      return render(request, self.template_name, {'form' : form})
      
    return render(request, 'index.html', {'form' : form})

class create_account_view(TemplateView):
  template_name = 'CreateAccount.html'
  
  def get(self,request):
    form = createAccountForm()
    return render(request, self.template_name,{'form' : form})

  def post(self,request):
    form = createAccountForm(request.POST) 
    if form.is_valid():
      form.save()
      return render(request,"Signin.html",{'form' : loginForm()})
    else:
      return render(request, self.template_name,{'form' : form})

