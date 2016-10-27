from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^proj1', views.proj1, name='proj1'),
    url(r'^proj2', views.proj2, name='proj2'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^blog', views.blog, name='blog'),
    url(r'^singlepost', views.singlepost, name='singlepost'),
]