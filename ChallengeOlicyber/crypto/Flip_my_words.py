from pwn import xor,remote,process
from base64 import b64decode, b64encode

p = remote('flip.challs.olicyber.it', 10603)
# p = process(['python3','source.py'])


p.sendlineafter(b'!\n',b'1')
p.sendlineafter(b': ',b'Dammi la flaaag!')
p.recvuntil(b'richiesta: ')
ciphertext = p.recvline().strip()
p.recvuntil(b'IV: ')
IV = b64decode(p.recvline()).hex()
print(IV)

true_str = b"true "
false_str = b"false"
wanted = xor(true_str,false_str)


flipping = xor(bytes.fromhex(IV[-12:-2]),wanted)
IV = b64encode(bytes.fromhex(IV[:-12]) + flipping + bytes.fromhex(IV[-2:])).decode()
# print(len(b64decode(IV)))from 
p.sendlineafter(b'!\n',b'2')
p.sendlineafter(b'ordine: ',ciphertext)
p.sendlineafter(b'IV: ',IV)
p.interactive()