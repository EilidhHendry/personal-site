"""PersonalSite URL Configuration

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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from redactor import urls as redactor_urls
from home import views as homeviews
from blogengine import views as blogengineviews

urlpatterns = [
    url(r'^$', homeviews.index, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about-me/', homeviews.about_me, name='about_me'),
    url(r'^resume/', homeviews.resume, name='resume'),
    url(r'^projects/', homeviews.projects, name='projects'),
    url(r'^blog/', blogengineviews.getRecentPosts, name='blog'),
    url(r'^post/(?P<pk>[0-9]+)/$', blogengineviews.post_detail, name='post_detail'),
    url(r'^redactor/', include(redactor_urls)),
]

urlpatterns += staticfiles_urlpatterns()
