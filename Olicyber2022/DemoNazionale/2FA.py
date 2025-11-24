from pwn import remote
from hashlib import sha256
from Crypto.Cipher import AES


p = remote('2fa.challs.olicyber.it', 12206)
p.sendlineafter(b'Esci\n',b'3')
p.recvuntil(b'admin:')
token = bytes.fromhex(p.recvline().strip().decode())
def expand_pin(pin):
    return sha256(pin).digest()[:16]


c2s = {}
for i in range(1_000_000):
    pin2 = str(i).zfill(6)
    print(f"Pin2 trying: {pin2}")
    c2 = AES.new(expand_pin(pin2.encode()), AES.MODE_ECB)
    c2s[c2.encrypt(b"donttrustgabibbo")] = pin2
    

c1s = []
for i in range(1_000_000):
    pin1 = str(i).zfill(6)
    print(f"Pin1 trying: {pin1}")
    c1 = AES.new(expand_pin(pin1.encode()), AES.MODE_ECB)
    if c1.decrypt(token) in c2s:
        pin2 = c2s[c1.decrypt(token)]
        
        break


p.sendlineafter(b'Esci\n',b'2')
p.sendlineafter(b'Username: ',b'admin')
p.sendlineafter(b'Pin personale: ',pin1.encode())
p.sendlineafter(b'Pin del server: ',pin2.encode())

p.interactive()