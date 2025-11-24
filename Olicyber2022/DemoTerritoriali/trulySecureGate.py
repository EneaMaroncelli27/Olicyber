from pwn import *

from pwn import *

elf = context.binary = ELF('./trulySecureGate')
context.terminal = ()
if args.REMOTE:
    p = remote('tsg.challs.olicyber.it', 14000)
elif args.GDB:
    p = gdb.debug(elf.path, gdbscript='''
        b checkPassword
        c
                               
    ''')
else:
    p = elf.process()


p.sendlineafter(b'$ ',b'cat flag.txt')

p.sendlineafter(b': ', b'hehethistimeyouwontfindthis')

p.interactive()