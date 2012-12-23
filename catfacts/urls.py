from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView

from catfacts import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'about/$', views.about, name='about'),
    url(r'^new_user/$', views.new_user, name='new_user'),
    url(r'^unsubscribe/$', views.unsub_user, name='unsubscribe'),
    url(r'^chat/$', views.chat, name='chat')
)