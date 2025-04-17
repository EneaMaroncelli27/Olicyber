from pwn import remote
from Crypto.Util.number import bytes_to_long, long_to_bytes
from binascii import unhexlify
from Crypto.Cipher import AES

r = remote('rsa.challs.olicyber.it', 10300)
r.recvuntil(b'p): ')
p = int(r.recvline().strip())
r.recvuntil(b'q): ')
q = int(r.recvline().strip())
r.recvuntil(b'e): ')
e = int(r.recvline().strip())

n = p * q
r.sendlineafter(b'n): ', str(n).encode())
phi = (p - 1) * (q - 1)
r.sendlineafter(b'n): ', str(phi).encode())
d = pow(e, -1, phi)
r.sendlineafter(b'd): ', str(d).encode())
r.recvuntil(b"'")
stringa = r.recvuntil(b"'", drop=True)

c = pow(bytes_to_long(stringa),e,n)

r.sendlineafter(b": ", str(c).encode())

r.recvuntil(b'IV: ')
iv = unhexlify(r.recvline().strip().decode())

r.recvuntil(b'CHIAVE: ')
key = unhexlify(r.recvuntil(b'\nTOKEN: ',drop=True).decode())
key = long_to_bytes(pow(bytes_to_long(key),d,n))

token = unhexlify(r.recvline().strip().decode())
cipher = AES.new(key, AES.MODE_CBC,iv)
plaintext = cipher.decrypt(token)
print(f'plaintext: {plaintext}', len(plaintext))

r.interactive()