from pwn import *

## dentro lo strlen xora con 0x2 tutti i caratteri dell username e pass

## memcpy xora con 0x40

## strcmp xora username+32 con 0x23 
## e username+1...   con il risultato

username = bytes.fromhex("E5FD8D2CD9026BC6E6CE892DC44239D6F0CE8B7BCC14050000000000000000008391EC4BA2715AA217")
password = bytes.fromhex("5DFEE6A141574D6C47C7B19F8628536E16CBDF6E515D99000000000000000000E6957A3D20F81C3B17")
flag = b""
usernameupd = b""
passwordupd = b""
for i in range(23):
    c = xor(username[i],username[32+(i%8)])
    flag += c
    usernameupd += xor(xor(c,0x40),0x2)


for i in range(23):
    if password[i] > password[32+(i%8)]:
        c = bytes([password[i]-password[32+(i%8)]])
    else:
        c = bytes([password[i]+0x100-password[32+(i%8)]])
    passwordupd += xor(xor(c,0x40),0x2)
    flag += c

print(flag.decode())
