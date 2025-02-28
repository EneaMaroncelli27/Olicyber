from pwn import *

p = remote("2048.challs.olicyber.it", 10007)
p.recvuntil(b":")
for i in range(0,2049):
    if i >= 2048:
       print(p.recvall())
    else:
        print(f"operazione numero {i}")
        op = p.recvuntil(b" ")
        print(op)
        s1 = p.recvuntil(b" ")
        s1 = s1.decode("utf-8")
        n1 = int(s1)
        s2 = p.recvuntil(b" ")
        s2 = s2.decode("utf-8")
        n2 = int(s2)
        print(n1,n2)
        if b"PRODOTTO" in op :
            payload = str(n1*n2).encode()
            p.sendline(payload)
        elif b"POTENZA" in op:
            payload = str(n1**n2).encode()
            p.sendline(payload)
        elif b"SOMMA" in op:
            payload = str(n1+n2).encode()
            p.sendline(payload)
        elif b"DIVISIONE" in op:
            payload = str(n1//n2).encode()
            p.sendline(payload)
        elif b"DIFFERENZA" in op:
            payload = str(n1-n2).encode()
            p.sendline(payload)
        