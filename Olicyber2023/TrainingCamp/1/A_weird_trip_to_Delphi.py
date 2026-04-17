from pwn import remote,xor

p = remote("trip-to-delphi.challs.olicyber.it", 34007)

p.recvuntil(b'= \'')
iv = p.recvline().strip().strip(b"\'").decode()
p.recvuntil(b'= \'')
enc_flag = p.recvline().strip().strip(b"\'").decode()

print(f"[*] ENC FLAG {enc_flag}")
print(f"[*] IV: {iv}")

new_byte = xor(bytes.fromhex(iv)[0],b'f')



new_iv = new_byte.hex() + iv[2:]
print(new_iv)

p.sendlineafter(b': ',new_iv.encode())
p.sendlineafter(b': ', enc_flag.encode())

p.recvuntil(b'= \'')
flag = bytes.fromhex(p.recvline().strip().strip(b"\'").split(b'00')[0].decode()).decode()

print(f"[*] FLAG = f{flag}")
