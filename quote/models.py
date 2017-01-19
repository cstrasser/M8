from django.db import models
#from m8connect.models import LineItem
from django.contrib.auth.models import User
 #import os
 #os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'm8connect.settings')
 #import django
#django.setup()

class M8_Item_Detail(models.Model): #additional information requied on an M8 part 
    M8UUID = models.CharField(max_length=38)
    costprice =  models.IntegerField()
    lastModified =  models.DateTimeField(auto_now=True)
    sellprice = models.IntegerField()
    vendor = models.CharField(max_length=60)
    

class Quote(models.Model):
    dateCreated = models.DateTimeField(auto_now_add = True)
    createdby = models.ForeignKey(User)
    m8_CustomerUUID = models.CharField(max_length=36)
    title  = models.CharField(max_length=80) #Quick one line title to describe the quotation
    description  = models.CharField(max_length=60) # preamble description visible to customer always works with title 
    related_M8UUID = models.CharField(max_length=38) # is there a related M8 Object ?
    total = models.IntegerField() #if fixed price we need this
    note = models.TextField()
    private_Note = models.TextField()
    active = models.BooleanField(default = True)    
    
class PO(models.Model):  #needs a merge method so we can send one PO for many jobs
    #vendor #M8 vendor or create our own vendor table ?? or Connect vendors from Xero ??
    dateIssued = models.DateField(auto_now=False, auto_now_add=True, ) # check this syntax
    notes = models.TextField()
    #status #open or closed sent .. are all items received    
    
class LineItem(models.Model):
    lineNumber  = models.IntegerField()
    item_M8UUID = models.CharField(max_length=36)
    qty = models.IntegerField()
    cost = models.IntegerField()
    multiplier = models.FloatField(default=1.522) #if multiplier set to 0 allow fixed price to stay multiplier only on quotes 
    price = models.IntegerField()
    hideOnPrint = models.BooleanField(default = False) # this way we can hide lines or prices on the printed quote or PO
    hidePriceOnPrint = models.BooleanField(default = False)
    isOption = models.BooleanField(default = False) # for quotes if this line will be in options section
    
   # class Meta:
    #    Abstract= True # needs abstract to allow Lineitem on both Quote and PO
    
   
class POLine(LineItem):
    po =models.ForeignKey(PO,on_delete=models.CASCADE) 
    associatedQuote = models.ForeignKey(Quote) #at this point it is an order but the original info is derived from the related quote
    #vendor = 
    vendor_part_number = models.CharField(max_length=30) #supplier part number
    purcasePrice = models.IntegerField() #final price we pay should be reco


    
    
    #signature  =  add signature line to quote at end
    #status #open or closed sent .. are all items received    


class Quoteline(LineItem): #need to attach each line item in a quote to the quote ... I think ...
    quote = models.ForeignKey(Quote,on_delete=models.CASCADE)
    

class Company(models.Model): 
    uuid =	models.CharField(max_length=38, primary_key = True)
    active = models.BooleanField()    
    edit_date =	models.DateTimeField()
    name =	models.CharField(max_length=100)
    abn_number	=	models.CharField(max_length=40) # austrailian business number 
    is_individual = models.CharField(max_length=40)
    address_street = models.CharField(max_length=60)
    address_city = models.CharField(max_length=60)
    address_state =	models.CharField(max_length=25)
    address_postcode = models.CharField(max_length=10)	
    address_country	= models.CharField(max_length=25)
    fax_number = models.CharField(max_length=16)
    address	= models.CharField(max_length=60)
    billing_address	= models.CharField(max_length=250)
    badges = models.CharField(max_length=250)
    tax_rate_uuid =	models.CharField(max_length=38)
    parent_company_uuid	= models.CharField(max_length=38, default ="")
    
    def __str__(self):
        return self.name
  
class Company_Contact(models.Model):
    uuid = models.CharField(max_length=38, primary_key=True)
    active = models.BooleanField()  
    edit_date =models.DateTimeField()	
    company_uuid = 	models.ForeignKey(Company)
    first = models.CharField(max_length=40) #	First name	
    last = models.CharField(max_length=40) #	Last name	
    phone = models.CharField(max_length=16)
    mobile = models.CharField(max_length=16)
    email = models.EmailField()
    contact_type = models.CharField(max_length=60)
    is_primary_contact = models.CharField(max_length=38)
    
    def __str__(self):
        return (self.first + ' ' + self.last)
    
