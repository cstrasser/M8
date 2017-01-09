import requests
import json
from django.shortcuts import render
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth

def hello(request):
    staff_list = []
    response = requests.get('https://api.servicem8.com/api_1.0/staff.json',auth=HTTPBasicAuth('cstrasser@secureway.ca','1010Security')) 
    
    for w in (json.loads(response.text)):   
        staff = dict(w)
        if staff['active'] ==1: 
            staff_list.append(staff)
       
    return render(request, 'index.html', {'staff_info': staff_list})
   
#dictlist = [dict() for x in range(n)]
#stafflist = [dict() for x in range(json.loads(response.text))]

#list[1]['d']




