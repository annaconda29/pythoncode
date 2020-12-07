import requests
import json
response =  requests.get("http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow")
print(response.json())