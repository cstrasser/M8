from . import views
from django.conf.urls import url




urlpatterns = [
    
    url(r'inventory/$', views.inventory, name ='inventory'),
    url(r'^customers/$', views.customers, name ='customers'),
    url(r'^jobs/$', views.jobs, name ='jobs'),
    #url(r'^hi/$', views.hello_pdf, name ='pdf'),
   
    
 ]