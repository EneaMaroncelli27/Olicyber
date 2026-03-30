from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from tqdm import trange

ct = "b5609cfbad99f1b20ec3a93b97f379d8426f934ffcb77d83ea9161fefa78d243"

for i in trange(10000000000000000):
    k = str(i).zfill(16)[::-1]
    print(k)
    cipher = AES.new(k.encode(),AES.MODE_ECB)
    f = cipher.decrypt(bytes.fromhex(ct))
    print(f)
    try:
        if f.decode().startswith('flag'):
            print(f)
            break
    except:
        pass