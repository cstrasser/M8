from django.db import models

class M8_Item_Detail(models.Model):
    M8UUID = models.CharField(max_length=36)
    Costprice =  models.IntegerField()
    LastModified =  models.DateTimeField(auto_now=True)
    Sellprice  models.IntegerField()
    Vendor = models.Charfield(max_length=60)
    
class Quote(models.Model):
    Title  = models.CharField(max_length=60)
    Description  = models.CharField(max_length=60)
    related_M8UUID = models.CharField(max_length=36)
    number = models.IntegerField() # or use m8 numbers ??
    M8_CustomerUUID = models.CharField(max_length=36)
    
class QuoteLineItem(models.Model):
    Quote = models.ForeignKey(Quote,on_delete=models.CASCADE)
    LineNumber  = models.IntegerField()
    Item_M8UUID = models.CharField(max_length=36)
    QuoteCost  models.IntegerField()
    QuotePrice  models.IntegerField()
    HideOnPrint = models.BooleanField(default = True) # this way we can hide lines or prices on the printed quote
    HidePriceOnPrint = models.BooleanField(default = True)
    
class PO(models.Model)
    Vendor #M8 vendor or create our own vendor table ?? or Connect vendors from Xero ??
    DateIssued = models.DateField(auto_now=False, auto_now_add=True, ) #
    Notes = models.CharField(max_length=250)
    Status #open or closed sent .. are all items received
  
class PO_Lineitem(models.Model) #needs a merge method so we can send 
    From_Quote = models.ForeignKey(Quote,on_delete=models.CASCADE) #at this point it is an order but the original info is derived from the related quote
    Line_number = models.IntegerField()
    Item_Number = models.CharField(max_length=30) #supplier part number
    Item_Description  = models.CharField(max_length=250)
    AgreedPrice = models.IntegerField() #final price we pay should be recorded in PO we can default from item detail costprice
    
    
