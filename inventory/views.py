import requests
import json
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth
from django.http import HttpResponse
from django.shortcuts import render
from m8connect.m8requests import m8ListRequest


def inventory(request):
    inventory_list = m8ListRequest('inventory')
    return render(request, 'inventory.html', {'message':'This  is a test message','inventory_list': inventory_list.data})

def customers(request):
    customer_list = m8ListRequest('customers')           
    return render(request, 'customers.html', {'customer_list': customer_list.data})

def jobs(request):
    job_list = m8ListRequest('jobs')
    return render(request, 'jobs.html', {'jobs_list': job_list.data})
 


