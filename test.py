import requests
import os
import json
import pandas as pd

with open('key', 'r') as key: 
    key = key.read()

with open('urls', 'r') as urls:
    urls = [x.strip() for x in urls.readlines()]

def testPls():
    url = (f"https://api.similarweb.com/capabilities?api_key={key}")
    response = requests.request("GET", url, headers={}, data={})
    return response.text

def getData():
    for url in urls:
        if os.path.exists(f'2021_json/{url}.json'):
            pass
        else:
            with open(f"json/{url}-2021.json", "w") as outfile:
                json.dump(requests.get(
                f"https://api.similarweb.com/v1/website/"
                f"{url}/total-traffic-and-engagement/visits?api_key="
                f"{key}&start_date=2021-01&end_date=2021-12&"
                f"country=gb&granularity=daily&"
                f"main_domain_only=false&format=json"   
                ).json(), outfile, indent=4)

# print(testPls())
getData()