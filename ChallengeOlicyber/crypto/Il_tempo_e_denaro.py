import time
from pwn import remote,process
from Crypto.Util.number import bytes_to_long, long_to_bytes, getStrongPrime

p = process(['python3','challenge.py'])
p = remote('time.challs.olicyber.it', 10505)

bitflag = ""
for i in range(25*8):
    p.sendlineafter(b'> ',b'1')
    start = time.time()
    p.sendlineafter(b'? ',str(i).encode())
    p.recvline()

    time_spent = time.time() - start
    if time_spent > 0.187:
        bitflag += "1"
    else:
        bitflag += "0"
    print(f"Time spent {time_spent} adding {bitflag[-1]}")
    
print(f"Flag found: {long_to_bytes(int(bitflag,2))}")
    

