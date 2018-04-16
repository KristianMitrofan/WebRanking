from django.conf.urls import url
from . import views

urlpatterns = [
    #/rankings/
    url(r'^$', views.homepage, name = 'homepage'),
    url(r'^rankings/$', views.index, name = 'index'),
    url(r'^matches/$', views.matches, name='matches'),
    url(r'^addmatch/$', views.addmatch, name='addmatch'),
    url(r'^aboutme/$', views.aboutme, name = 'aboutme'),
]