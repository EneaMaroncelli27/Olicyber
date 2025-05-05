from pwn import remote
import string
p = remote('geroglifici.challs.olicyber.it', 35000)

alphabet = string.ascii_letters + string.digits + "_{}!"
print(alphabet)
p.recvuntil(b'recita ')
flag_enc = p.recvline().decode('utf-8')
p.sendlineafter('> ', alphabet.encode())
alph_encode = {}
for i in range(66):
    lett = p.recv(4).decode('utf-8')
    alph_encode[alphabet[i]] = lett

print(alph_encode)
flag = ''
for j in range(len(flag_enc)):
    for k ,v in alph_encode.items():
        if v == flag_enc[j]:
            flag += k 
print(flag)
p.close()