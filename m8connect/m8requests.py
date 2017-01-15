'''Module to define classes of retrieval methods for service M8
1) lists class that gets a dict  is it parts prople or whatever and then does it inlude a filter value
2) item class that requests individual item so dict needs to contain uuid
'''
import requests
from requests.auth import HTTPBasicAuth
import json
import os

 #M8BASE ='https://api.servicem8.com/api_1.0'
m8_Key = os.environ['CJSM8']
USER = 'cstrasser@secureway.ca'
#http://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python

class m8ListRequest():
   
    def __init__(self, *args, **kwargs):
        #args carrys the key to the m8map above  kwargs carries a filter value if sent eg 'filter':'filter for this'
        request_List = []
        thisFilter = ' '
        m8Map = {'inventory':'https://api.servicem8.com/api_1.0/Material.json',
                'contacts':'https://api.servicem8.com/api_1.0/CompanyContact.json',
                'jobs':'https://api.servicem8.com/api_1.0/Job.json',
                'customers':' https://api.servicem8.com/api_1.0/Company.json'}
        #http://developer.servicem8.com/docs/rest-api/filtering/
        #field ,operator, value
        #curl -u email:password "https://api.servicem8.com/api_1.0/
        #job.json?%24filter=company_uuid%20eq%20'10420f98-7626-4405-bf43-043f1036623b'"
        self.filteron = kwargs.get('filteron',None)#none is default if nothing sent thru kwargs
        if self.filteron: #not finished ..if there is a filtervalue append it to the request
            
            field  = kwargs.get('filteron')
            operator = kwargs.get('operator')
            value = kwargs.get('value')
            thisFilter = '?%24filter='+ field + '%20'+ operator +'%20' + "'" +value +"'"
            thisRequest= m8Map[args[0]]
            print ('filter',thisFilter)
            self.response= requests.get(thisRequest + thisFilter, auth=HTTPBasicAuth(USER,m8_Key))
        else: #if no filter then get the whole list
            thisRequest = m8Map[args[0]]
            self.response= requests.get(thisRequest, auth=HTTPBasicAuth(USER,m8_Key))
    
        if self.response.status_code != 200:
            raise Exception('m8ListRequest fail code:' ,self.response.status_code)
        for w in (json.loads(self.response.text)):   
            item = dict(w)
            request_List.append(item)
        self.data = request_List
       
        '''http://developer.servicem8.com/docs/rest-api/filtering/
        curl -u email:password "https://api.servicem8.com/api_1.0/job.json?%24filter=
        company_uuid%20eq%20'10420f98-7626-4405-bf43-043f1036623b'''


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
    
            
class m8ItemCreate(request):
          m8Map = {'inventory':'https://api.servicem8.com/api_1.0/Material/',
                'contact':'https://api.servicem8.com/api_1.0/CompanyContact/',
                'job':'https://api.servicem8.com/api_1.0/Job/',
                'customer':'https://api.servicem8.com/api_1.0/Company/'}
        pass
        #to be completed after demo account set up
        
        
          

if __name__ == '__main__':
   ID= '6813494b-0088-4c27-baac-e5732a4ff14b' #(mallorytown KOA)
   mylist = m8ListRequest('jobs',filteron ='company_uuid', operator = 'eq',value = ID )
   for blah in mylist.data:
    print(blah['payment_method'])
   #customer = m8ItemRequest('customer',ID)
   #print(customer.data['name'])
   #print(customer.data['address'])
  
   
   
      
   