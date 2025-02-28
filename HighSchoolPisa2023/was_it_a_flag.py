import requests

url = 'http://was-it-a-flag.challs.olicyber.it/flag.php'
payload = {
    "password" : "eyes"
}
r = requests.post(url=url,data=payload, allow_redirects=False)
print(r.text)