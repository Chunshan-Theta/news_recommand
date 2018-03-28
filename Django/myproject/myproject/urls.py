"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))


"""
from django.conf.urls import include, url
from django.contrib import admin
from DemoProject.views import hello_world
from DemoProject.views import UsingStaticSource
from DemoProject.views import Http_From_Get
from DemoProject.views import Http_From_Post
from DemoProject.views import For_Cycle
from DemoProject.views import SQL_test
from DemoProject.views import SQL_all



urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^Demo/$', hello_world),
    url(r'^Demo/static_url/$', UsingStaticSource),
    url(r'^Demo/Cycle/$', For_Cycle),
    url(r'^Demo/Get/(?P<input1>\S*)/(?P<input2>\S*)/$', Http_From_Get),#http://....../Demo/Get/HELLO/WORLD/
    url(r'^Demo/Post/$', Http_From_Post),
    url(r'^Demo/SQL/(?P<c>\S*)/$', SQL_test),
    url(r'^Demo/SQL/$', SQL_all),


]
