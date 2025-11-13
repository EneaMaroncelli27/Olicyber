from pwn import remote
from sympy import sqrt_mod

q = 5371695748955787613 
cookie = b'admin=False&user=ciao'

cookie_blocks = [cookie[i*8:(i+1)*8] for i in range(len(cookie)//8 + 1)]
t1 = int.from_bytes(cookie_blocks[0]) % q

## sistema tra i tre tag 
# t2*k+v[2] = t3 mod(q)
# t1*k+v[1] = t2 mod(q)
# t1 = v[0] mod(q)

# t3 è noto perche è il tag finale e t1 anche perche all'inizio tag=0 quindi è uguale a v[0]%q --> sostiuisco

# (v[0]*k +v[1])*k +v[2] = t3 mod(q)
# v[0]k^2 + v[1]k + (v[2] - t3) = 0 mod(q)

p = remote('notpoly.challs.olicyber.it', 35001)

p.sendlineafter(b'> ',b'2')
p.sendlineafter(b'? ','ciao')
p.recvuntil(b'.')
t3 = int(p.recvline().strip())

vs = []

for b in cookie_blocks:
    vs.append(int.from_bytes(b) % q)


delta = (vs[1]**2 - 4*vs[0]*(vs[2]-t3)) % q

rad = sqrt_mod(delta,q) # radice di un numero con modulo primo


k = ((-vs[1] + rad)*pow(2*vs[0],-1,q)) % q # --> invece che dividere per v[0]*2 faccio moltiplicazione per l'inverso moltiplicativo
if k < 0:
    k = ((-vs[1] - rad)*pow(2*vs[0],-1,q)) % q

t1 = vs[0] % q
t2 = (t1*k + vs[1]) % q
t3_check = (t2*k + vs[2]) % q

adt_cookie = b'admin=True&user=ciao'
adt_blocks = [adt_cookie[i*8:(i+1)*8] for i in range(len(adt_cookie)//8 + 1)]
vs = []
for b in adt_blocks:
    vs.append(int.from_bytes(b) % q)

t1 = vs[0] % q
t2 = (t1*k + vs[1]) % q
t3_firmed = (t2*k + vs[2]) % q

p.sendlineafter(b'> ',b'1')

cookie = adt_cookie+b'.'+str(t3_firmed).encode()

p.sendlineafter(b': ', adt_cookie+b'.'+str(t3_firmed).encode())
p.interactive()