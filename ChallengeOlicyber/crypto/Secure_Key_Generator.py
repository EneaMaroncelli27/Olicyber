from pwn import xor
from datetime import datetime
import random
from hashlib import sha256

def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big')


data = datetime(2021, 3, 21, 17, 37, 40)

timestamp = int(data.timestamp())

random.seed(timestamp)
h = sha256(int_to_bytes(timestamp)).digest()


seed = int_from_bytes(h[32:])
key = h[:32]

random.seed(seed)

for _ in range(32):
    key += bytes([random.randint(0, 255)])

with open("flag.enc", "rb") as f:
    flag_enc = f.read()

dec = xor(flag_enc, key)

with open("flag.pdf", "wb") as f:
    f.write(dec)

# flag nel pdf