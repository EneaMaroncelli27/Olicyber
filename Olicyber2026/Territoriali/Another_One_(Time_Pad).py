from pwn import xor,remote,process
import string
from base64 import b64decode
alph = string.ascii_letters + string.digits + "+/="

p = remote('another-one.challs.olicyber.it', 38081)
cts = []
for i in range(100):
    p.recvuntil(b'! ')
    cts.append(bytes.fromhex(p.recvline().strip().decode()))
    p.sendlineafter(b'> ',b"y")

possible_chars = []
for i in range(len(cts[0])):
    chars_for_idx = []
    for c in alph:
        char = xor(c.encode(),cts[0][i]).decode()
        if char in alph:
            chars_for_idx.append(c)
    possible_chars.append(chars_for_idx)

for i in range(1,len(cts)):
    for j in range(84):
        to_remove = []
        for c in possible_chars[j]:
            char = xor(c.encode(),cts[i][j]).decode()
            if char not in alph:
                to_remove.append(c)
        for c in to_remove:
            possible_chars[j].remove(c)

flag = ""

for e in possible_chars:
    flag += e[0]

print(b64decode(flag.encode() + b'=' * (len(flag)//4)))