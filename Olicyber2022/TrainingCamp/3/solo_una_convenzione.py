
import requests
url='http://convenzione.challs.olicyber.it/'
r = requests.request('FLAG' ,url=url)
print(r.headers)
