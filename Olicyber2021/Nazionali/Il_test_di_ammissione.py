from pwn import remote
import string
    
p = remote("test1.challs.olicyber.it", 15004)
alph = string.ascii_uppercase
while True:
    try:
        p.recvuntil(b"Livello")
        p.recvuntil(b':\n')
        stati = p.recvline().decode().strip().split()
        mosse = []
        while True:
            pulsanti = p.recvline().strip().decode().split()
            if not any(p in string.ascii_uppercase for p in pulsanti):
                print("finite")
                break
            mosse.append(pulsanti)
        corr = {}
        for i,s in enumerate(stati):
            corr[alph[i]] = int(s)
        print(corr)
        print(mosse)
        print(stati)
        solve = ""
        while True:
            changed = False
            for i,m in enumerate(mosse):
                if int(corr[m[0]]) < 5:
                    solve += f"{i+1} "
                    corr[m[0]] += 1
                    changed = True
            if not changed:
                break
        p.sendline(solve.encode())
    except EOFError:
        p.interactive()
        exit()