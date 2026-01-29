from pwn import remote
from tqdm import trange
p = remote("segreto.challs.olicyber.it", 33000)


max = {
    "max": 0,
    "string": ""
}
for h in range(10):
    bresponses = []
    try:
        print("Getting data... Round", h+1)
        for i in trange(255):
            p.sendlineafter(b'>',str(i).encode())
            resp = p.recv(16).strip()
            binary_resp = "{:08b}".format(int(resp.decode(),16))
            bresponses.append(binary_resp)
        max["max"] = 0
        max["string"] = ""
        for b in bresponses:
            n = b.count('1')
            if n > max["max"]:
                max["max"] = n
                max["string"] = int(b, 2).to_bytes(8, "big")
        print("Secret:", max["string"].hex())
        p.sendlineafter(b'>', b'g')
        p.sendlineafter(b'?', max["string"].hex().encode())
    except Exception as e:
        p.interactive()
        break
p.interactive()
