import requests, re

pattern = r"https://[\S]+.html"
res1 = requests.get(input())
res2 = requests.get(input())
links = []
links.extend(re.findall(pattern,res1.text))
#print(links)
links1 = []
if res1.ok and res2.ok:
    for link in links:
        res3 = requests.get(link)
        links1.extend(re.findall(pattern, res3.text))
else:
    print('No')
#print(links1)
#for i in links1:
if res2.url in links1:
    print('Yes')
else:
    print('No')
#print(res2.url)


