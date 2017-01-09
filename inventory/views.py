import requests
import json
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render

CJSM8_Key = os.environ['CJSM8']


def inventory(request):
    m8user = None
    if request.user.is_authenticated():
        m8user = request.user.email
    inventory_list = []
    response = requests.get('https://api.servicem8.com/api_1.0/Material.json',auth=HTTPBasicAuth('cstrasser@secureway.ca',CJSM8_Key)) 
    
    for w in (json.loads(response.text)):   
        item = dict(w)
        if item['active'] ==1: #only show active invnetory items
            inventory_list.append(item)
            
    return render(request, 'inventory.html', {'inventory_list': inventory_list})


def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
    temp = BytesIO()
    # Create the PDF object, using the StringIO object as its "file."
    p = canvas.Canvas(temp)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")
    p.line(100,100,200,100) #line
    p.drawString(105, 105, "Line 2")
    p.rect(100, 100, 50,50, stroke=1, fill=0) #rectangle
    
''' example on how to do lines of text in pdf file from the reportlab manual
# size = 7
#  y = 2.3*inch
#  x = 1.3*inch
#  for line in lyrics:
#  canvas.setFont("Helvetica", size)
#  canvas.drawRightString(x,y,"%s points: " % size)
#  canvas.drawString(x,y, line)'''
    # Close the PDF object cleanly.
    p.showPage()
    p.save()
    #return HttpResponse('Hi responsded')
    response.write(temp.getvalue())
    return response
