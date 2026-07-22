from pwn import remote,process
from Crypto.Util.Padding import pad
words = [
    "Girasole", "Tempesta", "Mistero", "Orologio", "Sussurro",
    "Fragile", "Caminetto", "Riflesso", "Labirinto", "Cristallo",
    "Nebbia", "Eclissi", "Farfalla", "Crepuscolo", "Onda",
    "Radice", "Specchio", "Melodia", "Ombra", "Incanto"
]
# p = process(['python3','secure_passphrase_generator.py'])
p = remote("spg.challs.olicyber.it", 38052)
p.sendlineafter(b'> ',b'1')
p.sendlineafter(b'? ',b"zaza")
username = pad(b"username=zaza;index0=0;index1=1;index2=2;index3=3",16)
print(len(username))
p.sendlineafter(b'> ',b'1')
p.sendlineafter(b'? ',username[9:])
p.recvuntil(b'-')
passphrase_f = p.recvuntil(b'-',drop=True).decode()
p.recvuntil(b'token: ')
token = p.recvline().strip()
p.sendlineafter(b'> ',b'2')
p.sendlineafter(b'? ',token[:160])
p.recvuntil(b'flag')
print("flag" + p.recvline().strip().decode().replace('-',''))
p.interactive()
