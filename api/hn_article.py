import requests
import json

# Make API call, store the response
url = 'https://hacker-news.firebaseio.com/v0/item/31353677.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Explore structure of data
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)
