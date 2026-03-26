from pwn import process,remote
tries = 0
while True:
    print(f"Try number {tries}")
    # p = process(["python3","challenge.py"])
    p = remote('cryptorland.challs.olicyber.it', 10801)
    vals = []
    lenghts = []
    for i in range(10):
        bin_val = bin(int(p.recvline().strip().decode()))[2:]
        vals.append(bin_val)
        lenghts.append(len(bin_val))

    max_len = max(lenghts)
    flag_bin = ""
    vals = ["0"*(max_len-len(v)) + v for v in vals]
    for i in range(max_len):
        vs = []
        vs.append(int(vals[0][i]))
        vs.append(int(vals[1][i]))
        vs.append(int(vals[2][i]))
        vs.append(int(vals[3][i]))
        vs.append(int(vals[4][i]))
        vs.append(int(vals[5][i]))
        vs.append(int(vals[6][i]))
        vs.append(int(vals[7][i]))
        vs.append(int(vals[8][i]))
        vs.append(int(vals[9][i]))
        
        if sum(vs) > 7:
            flag_bin += "1"
        else:
            flag_bin += "0"
        
    guess = str(int(flag_bin,2))
    p.sendlineafter(b'?', guess.encode())
    
    response = p.recvline()
    if not b"Nope" in response:
        print(response)
        p.interactive()
        exit()

    tries += 1
    p.close()
