from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path("registration",views.registration,name="registration"),
    path("contact",views.contact,name="contact")

]
