from pwn import remote,process


# p = process(['python3','challenge.py'])
p = remote("privateiv.challs.olicyber.it", 10021)


p.sendlineafter(b'> ',b'1')
p.sendlineafter(b':',b'00'*16 )
p.recvuntil(b': ')
flag_enc = p.recvline().strip()[:32]
print(flag_enc)
p.sendlineafter(b'> ',b'2')
p.sendlineafter(b':',b'00'*16 + flag_enc )
flag = p.recvline().strip()[32:].decode()

print(bytes.fromhex(flag))

p.interactive()