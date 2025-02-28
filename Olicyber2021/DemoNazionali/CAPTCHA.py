import requests
import pytesseract
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import requests.compat


session = requests.Session()
session.headers.update({
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0"
})

for i in range(0,100):
    if i == 0:
        url = 'http://captcha.challs.olicyber.it/'
    else:
        url = 'http://captcha.challs.olicyber.it/next'

    r = requests.get(url=url)
    soup = BeautifulSoup(r.text, 'html.parser')
    image_tag = soup.find('img')
    image_url = image_tag['src']
    image_url = requests.compat.urljoin(url,image_url)
    image_r = requests.get(image_url)
    image = Image.open(BytesIO(image_r.content))

    testo = pytesseract.image_to_string(image)
    testo = testo.replace(" ","")
    print(testo)
    url_risposta = 'http://captcha.challs.olicyber.it/next'
    data = { "risposta" : f'{testo}'}
    captcha = requests.post(url=url_risposta,data=data)
    print(captcha.text)
    break