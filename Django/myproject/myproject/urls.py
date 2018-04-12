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
from DemoProject.views import SQL_each
from DemoProject.views import SQL_all



urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^NewsTW/each/(?P<c>\S*)/$', SQL_each),
    url(r'^NewsTW/(?P<page>\S*)/$', SQL_all),
    url(r'^NewsTW/$', SQL_all,name="home"),


]
