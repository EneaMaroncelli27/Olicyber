from pwn import *

p = remote('lucky.challs.olicyber.it', 17000)

p.recvuntil('key: ')
p.sendline(b'1804289383') # Valore di rand() con seme 0
p.interactive()