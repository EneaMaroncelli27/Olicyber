import os
from zipfile import ZipFile

#    Wordlist rockyou.txt utile per casi di bruteforce come questo

with open("rockyou.txt","r",encoding="latin1") as file:
    pwd_list = [line.strip() for line in file]

def zip_bruteforce(pwd_list,zfile):       
       with ZipFile(f'{zfile}',"r") as zfile:
         for pwd in pwd_list:

            try:
                zfile.extractall(pwd=pwd.encode('latin1'))
                print(f"Estrazione file {zfile} riuscita con password {pwd}")
                break
            except:
                 continue
for i in range(100):
      flagfile = f"{100-i}.zip"
      zip_bruteforce(pwd_list,flagfile)
      #  Rimozione file contente il file estratto
      os.remove(f'{flagfile}')
       

            



