# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 19:54:44 2020

@author: owner
"""

#%%
import json as js
from urllib.request import urlopen
import xml.etree.ElementTree as ET 

#%%
people_string = '''
{
  "people": [
      {
       "name": "John Smith",
       "phone": "615-555-7164",
       "emails": ["johnsmith@bogusmail.com","john.smith@myplace.com"],
       "has_license": false
       },
      {
       "name": "Jane Doe",
       "phone": "717-555-4344",
       "emails": null,
       "has_license": true
       }
   ]
}
'''

data = js.loads(people_string)

print(data)

#%%
for person in data['people']:
    print(person['name'])
    person['phone'] = None # leaves the key with NULL when it converts
    # del person['phone'] # removes the entire entry

new_string = js.dumps(data,indent=2)

print(new_string)

#%%

xmlfile = 'animenewsnetwork.xml'

url = r'https://www.animenewsnetwork.com/encyclopedia/reports.xml?id=155&nskip=0&nlist=50'
with urlopen(url) as response:
    source = response.read()

with open(xmlfile, 'wb') as  f:
    f.write(source)

# print(source)
tree = ET.parse(xmlfile)

root = tree.getroot()

