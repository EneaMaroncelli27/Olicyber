import time,requests,random,string,hmac,hashlib
from datetime import datetime,timezone

site = 'http://trulyrandomsignature.challs.olicyber.it/'

s = requests.Session()
temp = time.time()
r = s.get(site)
headuptime = r.headers['X-Uptime']

timestamp = int(temp) - int(headuptime)

timestamp -= 500
for i in range(1000):
    timestamp += 1
    seed =  datetime.fromtimestamp(timestamp,tz=timezone.utc)
    seed = seed.strftime('%Y-%m-%d %H:%M:%S')
    letters = string.ascii_lowercase

    random.seed(seed)
    key = ''.join(random.choice(letters) for i in range(32))
    textAsBytes = bytes(r.cookies['user'], encoding='ascii')

    keyAsBytes  = bytes(key, encoding='ascii')
    signature = hmac.new(keyAsBytes, textAsBytes, hashlib.sha256).hexdigest()
    
    if signature == r.cookies['signature']:
        print("Trovata!!!"," ", signature,)
        break
assert signature == r.cookies['signature']    
textAsBytes = bytes('admin', encoding='ascii')
new_sign = hmac.new(keyAsBytes, textAsBytes, hashlib.sha256).hexdigest()

s.cookies.clear()
s.cookies.set('user','admin')
s.cookies.set('signature',new_sign)


r = s.get(site + 'admin',)
print(r.text)
