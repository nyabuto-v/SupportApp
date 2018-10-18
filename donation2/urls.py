# supportapp2/donation2/urls.py

from django.conf.urls import url
from donation2 import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    # url(r'^about/$', views.AboutPageView.as_view(), name='about'),

     url(r'^contact/$', views.contact, name='contact'),
     url(r'^contact2/$', views.ContactPageView.as_view(), name='contact2'),
]