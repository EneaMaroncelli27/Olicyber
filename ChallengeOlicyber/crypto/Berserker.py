from pwn import xor,remote,process,args
from Crypto.Util.Padding import pad


import string
alph =  '_{}' + string.digits + string.ascii_letters 
# alph = string.ascii_letters + string.digits + string.punctuation
p = process(['python3','challenge.py'])
if args.REMOTE:
    p = remote('berserker.challs.olicyber.it', 10507)
f = b''
for i in range(6,21):
    for c in alph:
        # print(f"Trying {c} at position {i}" )
        temp = c.encode() + f
        p.sendlineafter(b'> ',b'1')
        p.sendlineafter(b'? ',b'a'*i)
        p.recvuntil(b'cifrato: ')
        cookie = bytes.fromhex(p.recvline().strip().decode())

        p.sendlineafter(b'> ',b'2')
        fpadded = pad(temp,16)
        payload = xor(xor(fpadded,cookie[-16:]),cookie[-32:])
        p.sendlineafter(b'hex): ',payload.hex().encode())
        p.recvuntil(b'cifrato: ')
        res = p.recvline().strip().decode()
        
        if res[:32] == cookie[-16:].hex():
            f = temp
            break
    print(f"Leaking {f}")
for i in range(21,37):
    for c in alph:
        temp = c.encode() + f
        p.sendlineafter(b'> ',b'1')
        p.sendlineafter(b'? ',b'a'*i)
        
        p.recvuntil(b'cifrato: ')
        cookie = bytes.fromhex(p.recvline().strip().decode())
        p.sendlineafter(b'> ',b'2')
       
        t = xor(temp,cookie[-16:])
        payload = xor(t ,cookie[-48:-32])
       
        p.sendlineafter(b'hex): ',payload.hex().encode())
        p.recvuntil(b'cifrato: ')
        res = p.recvline().strip().decode()
        if res[:32] == cookie[-32:-16].hex():
            
            f = temp
            break
    print(f"Leaking {f}")          

print(f'Flag found: {'f'+f.decode()}')