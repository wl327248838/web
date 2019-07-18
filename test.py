import requests
import json

url = 'http://10.14.10.148/api/status'
method = 'GET'
response = requests.request(method, url)
payload = json.loads(response.content)
print (payload['code'])