import pandas as pd
from serpapi import GoogleSearch
import json

api_key =  "serp_api_key"
engine_search = "youtube"

#data analysis tools:
code_langs = [
    {"name":"engine", "query":"sql"},
    {"name":"engine", "query":"excel"},
    {"name":"engine", "query":"tableau"},
    {"name":"engine", "query":" microsoft azure"},
    {"name":"engine", "query":"amazon web services"},
    {"name":"engine", "query":"r programming"}
    #{"name":"engine", "query":"name_of_product"}   
]

data_vids = pd.DataFrame([])

for lang in code_langs:
    params = {
        lang['name']:engine_search, 
        "search_query": lang['query'],
        "api_key": api_key
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()
    playlist_results = results['video_results']
    data_vids = data_vids.append(pd.json_normalize(playlist_results), ignore_index = True)
    data_vids.to_csv('code_languages.csv')
