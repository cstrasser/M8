from . import views
from django.conf.urls import url




urlpatterns = [
    
    url(r'^$', views.inventory, name ='inventory'),
    url(r'^hi/$', views.hello_pdf, name ='pdf'),
   
    
 ]