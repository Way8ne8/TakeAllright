import requests, re

pattern = r"https://[\S]+html"
res1 = requests.get(input())
res2 = requests.get(input())
links = []
links.extend(re.findall(pattern, res1.text))
links1 = []
if res1.ok and res2.ok:
    for link in links:
        res3 = requests.get(link)
        links1.extend(re.findall(pattern, res3.text))
        if res3.ok:
            for link1 in links1:
                res4 = requests.get(link1)
                if res4.url == res2.url:
                    print('Yes')
                else:
                    print('No')
        else:
                print('No')
else:
    print('No')


