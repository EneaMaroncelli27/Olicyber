from pwn import *
from Crypto.Cipher import AES

elf = context.binary = ELF('./blockypics')

if args.REMOTE:
    p = remote('blockypics.challs.olicyber.it', 10805)
elif args.GDB:
    p = gdb.debug(elf.path, gdbscript='''
        b *main+190
    ''')
else:
    p = elf.process()

# valori presi da gdb
k1 = p64(0xf9d4f97ec32386ae) + p64(0x98e5a1d3582e93d2) + p64(0xbc4745cd89496416) + p64(0xfbb26994a011626a)
iv1 = p64(0x7ce0f1fbbe164591) + p64(0xe394dc1d320e2ddb)
k2 = p64(0x7d78ddc28188813c) + p64(0x0ab98a4131d78590) + p64(0x8aa008726b9a5aec) + p64(0x333c8b08092d9fa6)
iv2 = p64(0xdc5fcca9324724cb) + p64(0x5bd221742cd41c1b)
k3 = p64(0x576b74a42bfe5e95) + p64(0xccfc30c974c83d7b) + p64(0x2dcc937479637d4f) + p64(0xd8810a33997e9bd9)
iv3 = p64(0x8a2703c381c191a8) + p64(0x974288c19fc85a3b)
k4 = p64(0xea1b2804304fd17c) + p64(0xe8c6361bde273ba4) + p64(0x3988468a6c4c6fb2) + p64(0x610f660524b1eeb5)
iv4 = p64(0x103f3efa1de5b87b) + p64(0xb9eda0d53bcf5220)
k5 = p64(0x99373147d0c0574d) + p64(0x840a3f7a33a97158) + p64(0x0bf60c07846ec20e) + p64(0x3af337b44b00f470)
iv5 = p64(0x421b24bec6a90582) + p64(0x591dd6b2ff208f88)

keys = [(k1, iv1), (k2, iv2), (k3, iv3), (k4, iv4), (k5, iv5)]

blocchi = []
while True:
    try:
        p.recvuntil(b'****\n')
        r = p.recvuntil(b'\n****', drop=True).strip().decode()

        blocchi.append(bytes.fromhex(r))
    except Exception as e:
        print(e)
        break  
r = p.recvuntil(b'Likes', drop=True).strip().decode()  
blocchi.append(bytes.fromhex(r))
dec = []
for i in range(len(blocchi)):
    cipher = AES.new(keys[i][0], AES.MODE_CBC, keys[i][1])
    dec.append(cipher.decrypt(blocchi[i]))

data = b''.join(dec)
with open('flag.jpg', 'wb') as f:
    f.write(data)
