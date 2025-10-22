from pwn import *
from binascii import unhexlify
ciphers = []

while True:
    if len(ciphers) == 5:
        break
    p = remote('sme.challs.olicyber.it', 10506)

    p.sendlineafter(b'! ', b'a'*128)

    p.recvuntil(b': ')
    c = p.recvuntil(b'Grazie',drop=True).strip().decode()
 
    if not c[:128] in ciphers:
        print(c[:128])
        ciphers.append(bytes.fromhex(c))
    p.close()

    # p.interactive()

# print(ciphers)

for i in range(len(ciphers)):
    key = xor(ciphers[i][:128],(b'a'*64).hex().encode())
    print(key.hex())
    for j in range(len(ciphers)):
            try: 
                print(unhexlify(xor(ciphers[j][:128],key))) 
            except:
                 continue