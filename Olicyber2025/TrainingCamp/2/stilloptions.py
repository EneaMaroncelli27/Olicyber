import requests

site = 'https://stilloptions.challs.olicyber.it/'

data  = {"secret":"yhrwlduoasd"}
r = requests.options(site,json=data)

print(r.text)