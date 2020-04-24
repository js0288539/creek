# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:54:26 2020

@author: owner

hn_submissions.py

"""

#%% IMPORT
from operator import itemgetter
import requests

#%% FUNCTIONS


#%% DEFINES
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

#%% MAIN

r = requests.get(url)
if(r.status_code == 200):
    print(f"Request succeeded: {r.status_code}")
    
    submission_ids=r.json()
    submission_dicts = []
    for submission_id in submission_ids[:30]:
        # Make a seperate API call for each submission
        url = f"https://hacker-news.firebaseio.com/vo/item/{submission_id}.json"
        r = requests.get(url)
        print(f"id: {submission_id}\tstatus: {r.status_code}")
        response_dict = r.json()
        
        # Build a dictionary for each article.
        submission_dict = {
               'title': response_dict['title'],
               'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
               'comments': response_dict['descendants']
            }
        submission_dicts.append(submission_dict)
        
        submission_dicts = sorted(
                                    submission_dicts,
                                    key=itemgetter('comments'), 
                                    reversed=True
                                  )
        for submission_dict in submission_dicts:
            print(f"\nTitle: {submission_dict['title']}")
            print(f"Discussion link: {submission_dict['hn_link']}")
            print(f"Comments: {submission_dict['comments']}")
else:
    print(f"Request failed:    {r.status_code}")


