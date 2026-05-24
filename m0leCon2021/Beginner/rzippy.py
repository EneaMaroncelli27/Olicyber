import os, time
import subprocess

for i in reversed(range(999)):
    files = os.listdir()
    files.remove('sol.py')
    output = subprocess.run(f'file {files[0]}',text=True,shell=True,capture_output=True).stdout
    print(output)

    if "bzip2" in output and "was" not in output:
        import bz2
        with bz2.open(files[0],'rb') as f:
            data = f.read()
        with open(f"{i}","wb") as f:
            f.write(data)

    elif "WIM" in output or " 7-zip archive data" in output:
        o = subprocess.run(f'7z x {files[0]}',shell=True,capture_output=True)

    elif "gzip" in output:
        import gzip
        with gzip.open(files[0],'rb') as f:
            data = f.read()
        with open(f"{i}","wb") as f:
            f.write(data)

    elif " Zip archive data" in output :
        import zipfile
        with zipfile.ZipFile(files[0], 'r') as zip_ref:
            zip_ref.extractall()
            
    elif "tar" in output:
        import tarfile
        f = tarfile.open(files[0])
        f.extractall()
        f.close()
    
    elif "XZ" in output:
        o = subprocess.run(f"mv {files[0]} nigga.xz",shell=True,capture_output=True)
        o = subprocess.run(f"xz -d nigga.xz",shell=True,capture_output=True)
        o = subprocess.run(f"mv nigga nigga.xz",shell=True,capture_output=True)
        o = subprocess.run(f"xz -d nigga.xz",shell=True,capture_output=True)


        continue


    else:
        break

        

    os.remove(files[0])
    

with open('flag.txt','r'):
    print(f.read())