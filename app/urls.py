from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home, name="index"),
    url(r'^about/$', views.about, name="about"),
    url(r'^service/$', views.service, name="service"),
    url(r'^contact/$', views.contact, name="contact"),

]
