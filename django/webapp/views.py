from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from .models import Testtemp
from .import plots
from webapp.forms import *
import requests
from django.http import HttpRequest
#or from .models import (name of class)

''' Create your views here. '''

''' index page '''
def home_view(request):
		if request.user.is_authenticated:
				APIurl = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c3f7f9ebb4a78e437ec87f6a909dd3d0'
				city = 'Irvine'
				city_weather = requests.get(APIurl.format(city)).json()

				weather_data = {
        		'city' : city,
        		'temperature' : city_weather['main']['temp'],
        		'description' : city_weather['weather'][0]['description'],
        		'icon' : city_weather['weather'][0]['icon']
  			}
 				# print(args,kwargs)
 				# print(request.user)
				#if 'HTTP_X_REQUEST_WITH' in HttpRequest.META:
				print(weather_data)
				if request.is_ajax():
						return JsonResponse(weather_data, safe=False)
				return render(request, 'index.html', weather_data)
		else:
				return HttpResponseRedirect('/')
    
def uwu_view(request):
		if request.user.is_authenticated:
				return HttpResponseRedirect('/home')
		else:
				return render(request, 'uwuplants.html')

''' about page '''
def about_view(request, *args, **kwargs):
  print(args,kwargs)
  print(request.user)
  return render(request,"About.html")

''' contact page '''  
def contact_view(request, *args, **kwargs):
  print(args,kwargs)
  print(request.user)
  return render(request,"Contact.html",{})


''' graphs/plot of data '''
class SimpleGraphs(TemplateView):
  template_name='Graphs.html'

  def get_context_data(self,**kwargs):
    context = super(SimpleGraphs, self).get_context_data(**kwargs)
    context['object'] = plots.get_graph()
    return context
    

''' sign in page '''
'''
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
'''

'''create account page '''

class create_account_view(TemplateView):
  template_name = 'CreateAccount.html'
  

  def get(self,request):
    form = createAccountForm()
    return render(request, self.template_name,{'form' : form})

  def post(self,request):
    form = createAccountForm(request.POST) 
    if form.is_valid():
      #form.save()
      userObj = form.cleaned_data
      username = userObj['username']
      fname =  userObj['firstName']
      lname =  userObj['lastName']
      password =  userObj['password']
      email = userObj['email']
      if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        user = authenticate(username = username, password = password)
        return HttpResponseRedirect('/home')
      else:
        raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
      return render(request, self.template_name,{'form' : form})


'''get service woker as app/js when '/serviceworker.js' is called'''
def service_workers(request):
    response = HttpResponse(open("serviceworker.js").read(), content_type='application/javascript')
    return response


''' data collection page '''
class data_collection_view(TemplateView):
  template_name = 'data_collection.html'

  def get(self, request):
    data = request.POST
    print(data)
    print(type(data))
    return render(request, self.template_name, {})

  def post(self, request):
    data = request.POST
    print(data)
    print(type(data))
    return render(request, self.template_name, {})
