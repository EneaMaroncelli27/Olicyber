from pwn import remote
from Crypto.Util.number import getPrime, isPrime, long_to_bytes
from Crypto.Cipher import AES

p = remote('crypto-13.challs.olicyber.it', 30006)
# prime = getPrime(1024)
# while not isPrime((prime-1)//2):
#     prime = getPrime(1024)
# print(prime)
prime = 115937840225080206316032850507982962118623926808761509987516200584195292039486344715232636986563723209419853845763080277772995931335811625332979653030215459640874554053645298501181024960912014205432345524070197862028362862331635658417980149749735219130387917691032052414324732748119192465015065645086907543203
p.sendlineafter(b':', str(prime).encode())
g = 2
p.sendlineafter(b':', str(g).encode())
b = 3
B = pow(g, b, prime)
p.sendlineafter(b'. ', str(B).encode())
p.recvuntil(b'. ')
A = int(p.recvline().strip(),16)
p.recvuntil(b': ')
p.recvuntil(b': ')
IV = bytes.fromhex(p.recvline().strip().decode())
p.recvuntil(b': ')
msg = bytes.fromhex(p.recvline().strip().decode())
print(f'A: {A}')
print(f'IV: {IV}')
print(f'msg: {msg}')
shared = long_to_bytes(pow(A,b,prime))
print(len(shared))
print(len(IV))
cipher = AES.new(shared[:16], AES.MODE_CBC ,iv=IV)
flag = cipher.decrypt(msg)
print("FLAG: ",flag)

p.interactive()