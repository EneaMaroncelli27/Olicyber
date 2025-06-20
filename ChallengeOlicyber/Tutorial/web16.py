import requests,re,sys
from bs4 import BeautifulSoup

site = 'http://web-16.challs.olicyber.it'
visited = set()
sys.setrecursionlimit(1000000)

def dfs(url):
    r = requests.get(url)
    
    flag = re.search(r'\s*flag{[^}]+\}',r.text)
    if flag:
        print(flag.group())
        exit()
    soup = BeautifulSoup(r.text,'html.parser')

    tags = soup.find_all(name="a")
    for t in tags:
        if t.attrs['href'] in visited:
            continue
        visited.add(t.attrs['href'])
        
        dfs(site+t.attrs['href'])
dfs(site)