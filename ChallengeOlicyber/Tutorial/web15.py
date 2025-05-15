import requests,re
from bs4 import BeautifulSoup

site = 'http://web-15.challs.olicyber.it'

s = requests.Session()

r = s.get(site)

soup = BeautifulSoup(r.text,'html.parser')

tags = soup.find_all(name=['link','script'])
endpoints = []
for t in tags:
    try:
        endpoints.append(t.attrs['href'])
    except:
        endpoints.append(t.attrs['src'])

for e in endpoints:
    r = s.get(site + e)
    flag = re.search(r'flag{[^}]+\}',r.text)
    if flag:
        print(flag.group())