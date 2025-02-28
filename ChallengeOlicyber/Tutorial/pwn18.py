from pwn import * 

p = remote('software-18.challs.olicyber.it', 13001)
p.sendline()
for i in range(101):
        try:
            p.recvuntil(b'restituiscimi ')
            print(i)
            address = p.recvuntil(b' ').strip()
            #print(address)
            address = address.replace(b'0x',b'')
            _packing =  p.recvline()
            #print(_packing)
            if b'32' in _packing:
                address = p32(int(address,16))
                #print(f"address packkato = {address}")
            elif b'64' in _packing:
                address = p64(int(address,16))
                #print(f"address packkato = {address}")

            #print(p.recvline())
            p.send(address)
        except:
             print(i)
             p.interactive()
    
    