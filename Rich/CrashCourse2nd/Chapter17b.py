# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:02:21 2020

@author: owner
"""

import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+jason'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, repo_links, stars, labels = [],[],[],[]

for repo_dict in repo_dicts:
    r_name = repo_dict['name']
    r_url = repo_dict['html_url']
    r_link = f"<a href='{r_url}'>{r_name}</a>"
    repo_links.append(r_link)
    repo_names.append(r_name)
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# make the visualization

data = [{
       'type': 'bar',
       # 'x': repo_names,
       'x': repo_links,
       'y': stars,
       'hovertext': labels,
       'marker': {
              'color': 'rgb(60,100,150)',
              'line': {'width': 1.5, 
                       'color': 'rgb(25,25,25)'
                       }
           },
       'opacity': 0.6
    }]

my_layout = {
       'title': 'Most-Starred Python Projects on GitHub',
       'titlefont': {'size': 28},
       'xaxis': {
                    'title': 'Repository',
                    'titlefont': {'size': 24},
                    'tickfont': {'size': 14}
                 },
       'yaxis': {
              'title': 'Stars',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14}
              }
    }

fig = {'data': data,
       'layout': my_layout
       }
offline.plot(fig,filename='python_repos.html')
