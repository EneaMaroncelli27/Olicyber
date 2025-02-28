from pwn import *

elf = ELF('./sw-19')
if args.REMOTE:
    p = remote('software-19.challs.olicyber.it', 13002)
else:
    p = process([elf.path])

p.recvuntil(b'iniziare ...')
p.sendline(b'a')
while True:
    try:
        func = p.recvuntil(b':').strip()
        func = func.replace(b'->',b'').replace(b':',b'').strip()
        print(func)
        address = elf.sym[func]
        address = hex(address)
        print(address)
        p.sendline(address)
    except:
        p.interactive()
