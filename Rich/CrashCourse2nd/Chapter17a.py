# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:13:19 2020

@author: owner
"""

import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers = {'Accept': 'application/vnd.github.v3+jason'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
response_dict = r.json()

#%%

print(f"Total repositories: {response_dict['total_count']}")
repo_dicts = response_dict['items']
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

#%%
print("\nSelected information about the first repository:")
# {repo_dict['']}
# print(f"")
ul = "=-"*70
ul = ul + '='
for repo_dict in repo_dicts:
    print(ul)
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
