from pwn import remote
import math

p = remote("crypto-12.challs.olicyber.it", 30005)

p.sendlineafter(b"?",b'p-1')
p.recvuntil(b'discreto di ')
s = int(p.recvuntil(b' ',drop=True).strip())
p.recvuntil(b'base ')
b = int(p.recvuntil(b' ',drop=True).strip())

sol = math.log(s, b)
print(sol)
p.sendlineafter(b'?', str(int(sol)).encode())

p.recvuntil(b'discreto di ')
s = int(p.recvuntil(b' ',drop=True).strip())
p.recvuntil(b'base ')
b = int(p.recvuntil(b' ',drop=True).strip())
p.recvuntil(b'mod ')
m = int(p.recvuntil(b')',drop=True).strip())
for i in range(100):
    if pow(b, i, m) == s:
        sol = i
        break
print(sol)
p.sendlineafter(b'?', str(int(sol)).encode())
p.recvuntil(b'p = ')
fpar = int(p.recvuntil(b',',drop=True).strip())
p.recvuntil(b'g = ')
spar = int(p.recvuntil(b'.',drop=True).strip())
p.recvline()
A = p.recvline().split(b' ')[-1].strip().strip(b'.')
print(A)
sol = pow(spar,67,fpar)
p.sendlineafter(b'?', str(int(sol)).encode())
S = pow(int(A),67,fpar)
p.sendlineafter(b'?', str(int(S)).encode())
p.interactive()