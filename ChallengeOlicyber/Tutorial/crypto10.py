from pwn import remote
import numpy as np
p = remote('crypto-10.challs.olicyber.it', 30003)

mods = []
sols = []
for _ in range(5):
    p.recvuntil(b'% ')
    mod = int(p.recvuntil(b' = ', drop=True).strip().decode())
    mods.append(mod)
    sol = int(p.recvline().strip().decode())
    sols.append(sol)


# xi viene calcolato come l'inverso moltiplicativo di (M/mi) mod mi

incognite = []
M = int(np.prod(mods))

for i in range(5):
    inc = pow((M // mods[i]),-1,mods[i])
    incognite.append(inc)

prodotti = []
for i in range(5):
    prodotti.append(sols[i] * incognite[i] * (M // mods[i]))

x = sum(prodotti) % M
p.sendlineafter(b'? ', str(x).encode())
p.interactive()