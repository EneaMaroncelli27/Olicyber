from pwn import *
from ctypes import CDLL

elf = context.binary =  ELF('./magicbb')

context.terminal = ()

libc = CDLL('libc.so.6')
if args.REMOTE:
    p = remote('magicbb.challs.olicyber.it', 38050)
elif args.GDB:
    p = gdb.debug([elf.path], ''' 
    b main
    c
    ''' )
else:
    p = process([elf.path])

rnd_numbs = []
libc.srand(0x1337)
for i in range(500):
    rnd_numbs.append(libc.rand())
# print(rnd_numbs)


b_input = bytearray(bytes.fromhex('1f84e6290b29a50954607fb2ad6615796a522d688d89acffe95a771ce9ba0d12b0288d7c'))
def xor_func(v,random_number):
    for i in range(36):
        v[i]^=random_number&0xff
    return v

def sub_func(v,random_number):
    for j in range(36):
        v[j]= (v[j] - random_number&0xff) &0xff
    return v

def add_func(v,random_number):
    for q in range(36):
        v[q]= (v[q] + random_number&0xff) & 0xff
    return v

def rot_r_func(v,random_number):
    copy = v.copy()
    for k in range(36):
        v[k] = copy[(k-random_number % 36 + 36)%36]
    return v

def rot_l_func(v,random_number):
    copy = v.copy()
    for z in range(36):
        v[z] = copy[(z+random_number % 36)%36]
    return v

# 1f84e6290b29a50954607fb2ad6615796a522d688d89acffe95a771ce9ba0d12b0288d7c 
fs = ['xor','sub','add','rot_r','rot_l']
for s in reversed(range(0,500)):
    f = fs[s%5]
    if f == 'xor':
        b_input = xor_func(b_input,rnd_numbs[s])
    if f == 'add':
        b_input = add_func(b_input,rnd_numbs[s])
    if f == 'sub':
        b_input = sub_func(b_input,rnd_numbs[s])
    if f == 'rot_l':
        b_input = rot_l_func(b_input,rnd_numbs[s])
    if f== 'rot_r':
        b_input = rot_r_func(b_input,rnd_numbs[s])
        
p.recvline()
print(b_input)
print(b_input.hex())
p.sendline(b_input.hex().encode())



p.interactive()

