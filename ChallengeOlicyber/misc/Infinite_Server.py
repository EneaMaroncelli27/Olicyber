import requests
from bs4 import BeautifulSoup
import re
URL = 'http://infinite.challs.olicyber.it/'

s = requests.Session()
r = s.get(URL)
i = 0
while True:
    soup = BeautifulSoup(r.text,'html.parser')

    q = soup.find('p').text
    

    if "ART TEST" in r.text:
        print("ART")
        if "Rosso" in q:
            data = {
                "Rosso":""
            }
        elif "Blu" in q:
            data = {
                "Blu":""
            }
        elif "Verde" in q:
            data = {
            "Verde":""
            }
        r = s.post(URL,data=data)
        
        i +=1
      
    elif "MATH" in r.text:
        print("MATH")
        q = q.split(" ")
      
        n1 = int(q[2])
        n2 = int(q[-1][:-1])
        res = n1 + n2
        data = {
            "sum":res
        }
        r = s.post(URL,data=data)
        i += 1
    elif "GRAMMAR" in r.text:
        print("GRAMMAR")
        q = str(q).split("\"")
        l = q[1]
        p = q[-2]
        res = p.count(l)
        data = {
            'letter':res,
            'submit':"Submit"
        }
        r = s.post(URL,data=data)
        i += 1 
    else:
        flag = re.findall(r'flag{.*}',r.text)
        print(flag[0])
        break

    # input()