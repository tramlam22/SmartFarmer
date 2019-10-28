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
from django.urls import path
from django.conf.urls import url

from webapp.views import home_view
from webapp.views import about_view
from webapp.views import graphs_view
from webapp.views import contact_view
urlpatterns = [
    #path(r'',home_view, name='home'),
    #path(r'Main/',home_view, name='home'),
    #path('About/',about_view, name = 'about'),
    #path('Graphs/',graphs_view, name = 'graphs'),
    #path('Contact/',contact_view, name = 'contact'),
    #path('admin/', admin.site.urls),
    url(r'^$',home_view, name='home'),
    url(r'^Main/$',home_view, name='home'),
    url(r'^About/$',about_view, name = 'about'),
    url(r'^Graphs/$',graphs_view, name = 'graphs'),
    url(r'^Contact/$',contact_view, name = 'contact'),
    url(r'^admin/$', admin.site.urls),
]
