from pwn import remote,xor

p = remote('sandwichmaster.challs.olicyber.it', 30996)

msg = b'Im so good with sandwiches they call me mr Krabs'

p.sendlineafter(b'>',b'1')
p.sendlineafter(b': ',msg.hex()[:-32].encode())
p.recvuntil(b' = \'')
pen_block = bytes.fromhex(p.recvline().strip().strip(b'\'').decode())

p.sendlineafter(b'>',b'1')
block = xor(pen_block, bytes.fromhex((msg.hex()[-32:]))).hex()
p.sendlineafter(b': ',block.encode())

p.recvuntil(b' = \'')
correct_tag = p.recvline().strip().strip(b'\'').decode()

p.sendlineafter(b'>',b'2')
p.sendlineafter(b': ',correct_tag.encode())
p.interactive()
