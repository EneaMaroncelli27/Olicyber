import requests
url = 'https://giorgionfile.challs.olicyber.it/'
r = requests.request("FROB",url = url)
print(r.text)