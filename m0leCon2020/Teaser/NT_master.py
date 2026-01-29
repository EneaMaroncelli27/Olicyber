from pwn import remote

def gcd(a : int, b : int):

    while b > 0:
        a,b = b,a%b
    return a
    



def lcm(a: int, b : int, mcd : int):
    n = abs(a*b)
    lcm = n//mcd
    return lcm

p = remote("nt-master.challs.olicyber.it", 11001)

p.recvuntil(b'tests.')
sent  = False
while True:
    try:
        p.recvuntil(b'= ')
        N = int(p.recvline().decode().strip())

        for a in range(2,N):
            MCD = N % a
            if MCD == 0:
                MCD = a
            if a % MCD != 0:
                continue
            num = (MCD * (N - MCD))
            if num % a != 0:
                continue
            b =  num // a
            b = int(b)
            if gcd(a,b) != MCD:
                continue
            if b > a:
                t = a
                a = b
                b = t
            p.sendline(f"{a} {b}".encode())
            print(f"Sent: {a} {b} for N={N}")
            break
            
    except Exception as e:
        print(f"Error: {e}")
        p.interactive()
        exit()

        break



        
