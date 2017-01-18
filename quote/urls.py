from django.conf.urls import include,url
from . import views
urlpatterns = [
    
    url(r'^main/$', views.quotelist, name ='main'),
    url(r'^detail/$', views.customers, name ='quote_detail'),
    url(r'^new/$', views.new, name ='new'),
    url(r'^quotelist/(?P<wargs>\w+)/$', views.quotelist, name='quotelist') #need to have ?/p for redirect to be able to pass paramters
    #url(r'^hi/$', views.hello_pdf, name ='pdf'),
   
    
 ]