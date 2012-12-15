from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView

from catfacts import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^faq/$', views.faq, name='faq'),
)