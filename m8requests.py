'''Module to define classes of retrieval methods for service M8
1) lists class that gets a dict  is it parts prople or whatever and then does it inlude a filter value
2) item class that requests individual item so dict needs to contain uuid

 #http://developer.servicem8.com/docs/rest-api/filtering/
        #field ,operator, value
        #curl -u email:password "https://api.servicem8.com/api_1.0/
        #job.json?%24filter=company_uuid%20eq%20'10420f98-7626-4405-bf43-043f1036623b'"
  http://developer.servicem8.com/docs/rest-api/filtering/
        curl -u email:password "https://api.servicem8.com/api_1.0/job.json?%24filter=
        company_uuid%20eq%20'10420f98-7626-4405-bf43-043f1036623b'''
import requests
from requests.auth import HTTPBasicAuth
import json



import os
from sys import argv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '..settings')
import django
django.setup()

from models import Company,Company_Contact

 #M8BASE ='https://api.servicem8.com/api_1.0'
m8_Key = os.environ['CJSM8']
USER = 'cstrasser@secureway.ca'
#http://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python
def getname(uuid):
    foo = {}
    get = m8ListRequest('customers', filteron ='uuid', operator = 'eq' ,value = uuid)
    data = (json.loads(get.response.text)) 
    foo = {k: v for d in data for k, v in d.items()} #convert list of dict to dict
    if not foo:
        foo['name':] = 'no name'
        
    return {'name': foo['name']}
    
class m8ListRequest():
   
    def __init__(self, *args, **kwargs):#args carrys the key to the m8map above kwargs carries a filter value if sent eg 'filter':'filter for this'
        request_List = []
        thisFilter = ' '
        m8Map = {'inventory':'https://api.servicem8.com/api_1.0/Material.json',
                'contacts':'https://api.servicem8.com/api_1.0/CompanyContact.json',
                'jobs':'https://api.servicem8.com/api_1.0/Job.json',
                'customers':' https://api.servicem8.com/api_1.0/Company.json'}
        if args[0] == 'jobs':
            thisFilter = '?%24filter=active%20eq%20True' #only get active jobs  else we get 424 too many requests error
        self.filteron = kwargs.get('filteron',None)#none is default if nothing sent thru kwargs
        if self.filteron: 
            field  = kwargs.get('filteron')
            operator = kwargs.get('operator')
            value = kwargs.get('value')
            thisFilter = '?%24filter='+ field + '%20'+ operator +'%20' + "'" +value +"'"
            thisRequest= m8Map[args[0]]
            self.response= requests.get(thisRequest + thisFilter, auth=HTTPBasicAuth(USER,m8_Key))
        else: #if no filter then get the whole list
            thisRequest = m8Map[args[0]]
            self.response= requests.get(thisRequest, auth=HTTPBasicAuth(USER,m8_Key))
            
        if self.response.status_code != 200:
            raise Exception('m8ListRequest fail code:' ,self.response.status_code)
       
        mybuffer = (json.loads(self.response.text))
        if args[0] == 'jobs':#if we are getting jobs we need to replace company uuid wiht company name
            for x in mybuffer:#this no work .. trying to resolve name from uuid and add 'name':'company name ' to dict
                mybuffer['name'] = getname(x['uuid']) 
        self.data = (json.loads(self.response.text))
      
      
class m8ItemRequest():
    #jobs: https://api.servicem8.com/api_1.0/Job/{UUID}.json'
    def __init__(self, *args,**kwargs):
        m8Map = {'inventory':'https://api.servicem8.com/api_1.0/Material/',
                'contact':'https://api.servicem8.com/api_1.0/CompanyContact/',
                'job':'https://api.servicem8.com/api_1.0/Job/',
                'customer':'https://api.servicem8.com/api_1.0/Company/'}
        thisRequest = m8Map[args[0]] + args[1] + '.json' #first arg is request type 2nd arg is uuid of what you want
        self.response= requests.get(thisRequest, auth=HTTPBasicAuth(USER,m8_Key))
        if self.response.status_code != 200:
            raise Exception('m8ItemRequest fail code:' ,self.response.status_code)
        self.data = ((json.loads(self.response.text)))
    
            
class m8ItemCreate():
        m8Map = {'inventory':'https://api.servicem8.com/api_1.0/Material/',
                'contact':'https://api.servicem8.com/api_1.0/CompanyContact/',
                'job':'https://api.servicem8.com/api_1.0/Job/',
                'customer':'https://api.servicem8.com/api_1.0/Company/'}
        pass
        #to be completed later

def update_local_tables():
    companies = m8ListRequest('customers')
    contacts = m8ListRequest('contacts')
    for contact in contacts.data:
        for company in companies.data:
            if company['uuid']   == contact['company_uuid']:
                #ok we have a match here do the models processing
                person = Company_Contact()
                place = Company()
                place.uuid	= company['uuid']
                place.active =	company['active']
                place.edit_date =company['edit_date']	
                place.name	=company['name']
                place.website=	company['website']	
                place.abn_number =	company['abn_number']
                place.is_individual	=	company['is_individual']
                place.address_street=	company['address_street']	
                place.address_city	=	company['address_city']
                place.address_state	=	company['address_state']
                place.address_postcode	=	company['address_postcode']
                place.address_country	=	company['address_country']
                place.fax_number = company['fax_number']
                place.address = company['address']
                place.billing_address =	company['billing_address']
                place.badges = company['badges']
                place.tax_rate_uuid	=	company['tax_rate_uuid']
                place.parent_company_uuid =  company['parent_company_uuid']                         
                #ok now contact info update
                person.uuid	= contact['uuid']
                person.active = contact['actve']
                person.edit_date = contact['edit_date']
                person.company_uuid = place
                person.first = 	contact['first']
                person.last = contact['last']
                person.phone = contact['phone']		
                person.mobile = contact['mobile']		
                person.email = contact['email']	
                person.type = contact['type']		
                person.is_primary_contact = contact['is_primary_contact']		
                             
               
                print(contact['first'],contact['last'],'=>',person.first,person.last,
                      company['name'],'=>',place.name)
    pass # on login run this to update local customer and company tables with m8 data 

            
if __name__ == '__main__':
   ID = '6813494b-0088-4c27-baac-e5732a4ff14b' #(mallorytown KOA)
   ID = 'c9fa75ee-0b10-4514-b5d0-21757dd99ffb'
   #mylist = m8ListRequest('customers',filteron ='uuid', operator = 'eq',value = ID )
   companies = m8ListRequest('customers')
   contacts = m8ListRequest('contacts')
   for contact in contacts.data:
       for company in companies.data:
           if company['uuid']   == contact['company_uuid']:   
               print(contact['first'],contact['last'], company['name'])
               
           
       
   #print(companies.data[1])
   #print(contacts.data[1])
   
   #print (mylist.data)
   #customer = m8ItemRequest('customer',ID)
   #print(customer.data['name'])
   #print(customer.data['address'])
  
   
   
      
   