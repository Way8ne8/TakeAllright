import requests, sys

type = 'math'

for line in sys.stdin:
    link = requests.get(f'http://numbersapi.com/{int(line)}/{type}?json')
    data = link.json()
    #print(data)
    if data['found']:
        print('Interesting')
    else:
        print('Boring')

