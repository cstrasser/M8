from django.shortcuts import render, render_to_response , redirect
from django import forms
from django.contrib.auth import authenticate, login
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from main.models import Organization, Location,Contact

def logon(request):
    nuthin = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                print ('login user is active')
                return render(request,'inventory.html',{})
                #return redirect(request,'home.html',{})
            
            else:
                
                pass # Return a 'disabled account' error message
        else:
           pass#  Return an 'invalid login' error message.
            
    else:
        return render(request, 'loginform.html')
    
def about(request):
    return render(request, 'about.html')