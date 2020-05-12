# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:46:23 2020

@author: owner

hn_article.py

"""

#%% IMPORT
import requests
import json

#%% DEFINE
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'

#%% MAIN

r = requests.get(url)
print(f"Status Code: {r.status_code}")

response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open(readable_file,'w') as f:
    json.dump(response_dict, f, indent=4)
