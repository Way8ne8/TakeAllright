import re
import requests

pattern = r"<a.*href *=[\"\'\ ]*(\w*://)?((\w[a-zA-Z1-9\.\-\_]+)+\.\w+)"
(         r'<a.*?href=["|\'](.*?:\/\/)?(\w.*?)([/|:].*)?["|\'].*')
res1 = requests.get(input())
links = re.findall(pattern, res1.text)
d = []
for i in range(len(links)):
    d.append(links[i][1])
s = set(d)
s = sorted(s)
for l in s:
    print(l)