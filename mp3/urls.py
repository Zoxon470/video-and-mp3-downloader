from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^results/$', views.download_mp3, name='download_mp3')
]