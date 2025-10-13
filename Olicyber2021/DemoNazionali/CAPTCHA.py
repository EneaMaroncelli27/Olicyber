import pytesseract, requests, wget,os,re
from bs4 import BeautifulSoup

URL = 'http://captcha.challs.olicyber.it/'

session = requests.Session()

r = session.get(URL)
for i in range(100):
    
    soup = BeautifulSoup(r.text,'html.parser')
    img = soup.find('img')
    path = img.get('src')
    f_name = wget.download(URL+path, out="img.png")

    text = pytesseract.image_to_string(f_name,lang="eng")[:8]

    r = session.post(URL+'next', data={"risposta":text})
    os.remove(f_name)


flag = re.search(r'flag{.*}',r.text).group()
print()
print(flag)

    

