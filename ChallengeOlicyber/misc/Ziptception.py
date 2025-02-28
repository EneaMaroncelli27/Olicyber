import os
from zipfile import ZipFile

for i in range(3002):
    if i == 3001:
        os.system('cat flag.txt')
    else:
        flagfile = f"flag{3000-i}.zip"
        with ZipFile(f'{flagfile}','r') as zfile:
            zfile.extractall()
            print(f"File {flagfile} estratto con successo")
            os.remove(flagfile)