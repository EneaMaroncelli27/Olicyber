import requests
import re
site = 'https://training-camp.challs.olicyber.it/'
headers = {
    "X-Secret-Message":"flag"
}
r = requests.get(site,headers=headers)
print(r.text)
