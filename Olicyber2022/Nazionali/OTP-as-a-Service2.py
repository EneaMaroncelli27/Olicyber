from pwn import remote
from tqdm import trange
p = remote("otp2.challs.olicyber.it", 12306)
p.recvuntil(b'connessione\n')
min_counter = [1000]*71
for _ in trange(1000):
    p.sendline(b"e")
    flag_enc = p.recvline().strip().decode().split("-")
    for i in range(len(flag_enc)):
        min_counter[i] = min(min_counter[i],int(flag_enc[i]))


for c in min_counter:
    print(chr(c),end="")
