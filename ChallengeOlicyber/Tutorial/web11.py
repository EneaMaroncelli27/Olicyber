import requests
for i in range(5):
    session = requests.Session()
    data = {
        "username":"admin",
        "password":"admin"
    }
    site_login = 'http://web-11.challs.olicyber.it/login'
    r = session.post(site_login,json=data)
    csrf = r.text.replace('"status": "ok",','').replace('{','').replace('}','').replace('"csrf": ','').replace('"','').strip()
    print(csrf)
    flag_site = f'http://web-11.challs.olicyber.it/flag_piece?index={i}&csrf={csrf}'
    r = session.get(flag_site)
    print(r.text)