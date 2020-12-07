import requests
import json
response =  requests.get("http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow")
for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
        print()
    else:
        print("skipped")
    print()