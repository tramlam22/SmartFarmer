"""ebdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from webapp.views import home_view
from webapp.views import about_view
from webapp.views import SimpleGraphs
from webapp.views import contact_view
# from webapp.views import signin_view
from webapp.views import create_account_view
from webapp.views import service_workers  #new
from webapp.views import uwu_view
from webapp.views import data_collection_view #also new 
# from webapp.views import manifest

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^$',uwu_view, name='uwuplants'),
    url(r'^home/$',home_view, name='home'),
    #url(r'^home/$',home_view, name='home'),
    url(r'^About/$',about_view, name = 'about'),
    url(r'^Graphs/$',SimpleGraphs.as_view(), name = 'graphs'),
    url(r'^Contact/$',contact_view, name = 'contact'),
    url(r'^admin/', admin.site.urls),
    #url(r'^Signin/$',signin_view, name = 'signin' ),
    # url(r'^Signin/$', signin_view.as_view(), name = 'signin'),
    url(r'^Createaccount/$', create_account_view.as_view(), name = 'createaccount'),
    url('^serviceworker.js$', service_workers),#new
    #url(r'^Createaccount/$', create_account_view, name = 'createaccount'),
    url(r'^data_collection/$', data_collection_view.as_view(), name = "data_collection")

]
