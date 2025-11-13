import math,json,os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64decode
from pwn import remote

p = int.from_bytes(b'\xff'*800)
g = 2

data = f"{hex(g)[2:]} {hex(p)[2:]}"

r = remote('corrupted.challs.olicyber.it', 10604)
r.sendlineafter(b': ',data)

# GET A PRIVATE

a_data = json.loads(r.recvuntil(b'}'))
a_pub = int(a_data['A'])
a_priv = int(math.log(a_pub,g))

# GET B PRIVATE

b_data = json.loads(r.recvuntil(b'}'))
b_pub = int(b_data['B'])
b_priv = int(math.log(b_pub,g))


r.recvuntil(b': ')
flag_enc = b64decode(r.recvline().strip().decode())
a_secret = pow(b_pub, a_priv, p)
b_secret = pow(a_pub, b_priv, p)
assert(a_secret == b_secret)

ab_secret =pow(g, a_priv * b_priv, p)
key = (ab_secret % (2**(8*16) - 1)).to_bytes(16, 'big')
cipher = AES.new(key, AES.MODE_ECB)
print(cipher.decrypt(pad(flag_enc,16)))

r.interactive()