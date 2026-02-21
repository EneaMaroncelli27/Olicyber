from pwn import remote
import time,random

p = remote("otp1.challs.olicyber.it", 12304)

timestamp_connessione = int(time.time())
p.sendlineafter(b"connessione\n",b"e")
flag_enc = p.recvline().strip().decode().split("-")


for i in range(timestamp_connessione-500,timestamp_connessione+500):
    random.seed(i)
    dec = ""
    for b in flag_enc:
        r = random.randint(0,255)
        b = int(b)
        if b - r < 0:
            dec += chr(b-r + 256)
        else:
            dec += chr(b-r)
    if dec.startswith("flag"):
        print(dec)
        exit()
    