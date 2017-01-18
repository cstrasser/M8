from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from m8connect.m8requests import m8ListRequest
from quote.models import Quote

@login_required
def quotelist(request):
    data = Quote.objects.all().filter(active = True)
    print ('got here ')
    import pdb
    pdb.set_trace() # start debugger
    if data:
        print ('sgfsgdsgdsfgdsfg',data)
        response = {'data':data}
    else:
        response ={'message': "No quotes found"}
        print ("nothing found and message should show up")
    return render(request, 'quotelist.html', response)
    
def new(request):
     p= Quote(createdby =user,m8_CustomerUUID = '6813494b-0088-4c27-baac-e5732a4ff14b',
              title ='Installation of Security System',total = 12345.65)
     print(p)
    
def customers(request):
    pass

def new(request):
    print('=========================================click got us here ')
   
    return render(request,'quote/quotelist.html',{})
    #return HttpResponseRedirect(request.GET.get('next')))
