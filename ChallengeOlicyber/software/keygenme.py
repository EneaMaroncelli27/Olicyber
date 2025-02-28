from pwn import *

p = remote('keygenme.challs.olicyber.it' ,10017)
p.recvuntil('User id: ')
id = p.recvline().decode().strip()
id = id.split('-')
id1 = id[0]
id2 = id[1]
id3 = id[2]
p.recvuntil('chiave.')
payload = ''
for i in range(0,16):
    if i % 2 == 0:
        payload += id3[i//2]
    else :
        payload += id2[i//2]

for i in range(0,16):
    if i % 2 == 0:
        payload += id1[i//2]
    else :
        payload += id3[i//2]
for i in range(0,16):
    if i % 2 == 0:
        payload += id2[i//2]
    else :
        payload += id1[i//2]

p.sendline(payload)
p.interactive()