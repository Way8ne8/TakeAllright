import requests
import json, sys
d ={}
with open('dataset_24476_4.txt') as f:
    read = f.read().splitlines()
headers = {"X-Xapp-Token" : 'eyJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOiI2MGVhZjE4MDI2MmE4MTAwMGUzMmI5OWMiLCJleHAiOjE2MjY2MTQ3ODQsImlhdCI6MTYyNjAwOTk4NCwiYXVkIjoiNjBlYWYxODAyNjJhODEwMDBlMzJiOTljIiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjYwZWFmMTgwMjE2ZTFiMDAwZTRmNjQxNCJ9.7Q94Pc85tdQVxNoMnP8nwdpct3b0uy5Dm3PcHyIjoFw'}
for x in read:
    link = requests.get(f'https://api.artsy.net/api/artists/{x}', headers=headers)
    link.encoding = 'utf-8'
    j = link.json()
    d[j['sortable_name']] = j['birthday']
    #print(j)
sorted(d.items(), key= lambda x:(x[1],x[0]))
for key, values in sorted(d.items(), key= lambda x:(x[1],x[0])):
    print(key)