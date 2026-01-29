from pwn import xor

class LFSR(object):
    def __init__(self, s):
        self.s = list(map(int, s))

    def gen_stream(self, n):
        out = []
        for i in range(n):
            out.append(self.s[0])
            self.s = self.s[1:] + [self.s[0]^self.s[3]^self.s[7]^self.s[9]]
            
       
        return out

flag_enc = "7dc0bc0397aa6f7c412f99720039840e6e1749072f9e350189c14cc12cff"

flag_prefix = bytes.fromhex(flag_enc)[:5] 

key_prefix_byte = xor(flag_prefix,b"flag{")

partial_initial_state = ""
for b in key_prefix_byte:
    partial_initial_state += bin(b)[2:].rjust(8,"0")


for i in range(2**16):
    candidate = bin(i)[2:].rjust(16,"0")
    print(candidate)
    s = partial_initial_state + candidate
    initial_state = [int(x) for x in s.rjust(56, '0')]
    L = LFSR(initial_state)
    k = b""

    for i in range(30):
        k += bytes([int("".join(str(x) for x in L.gen_stream(8)), 2)])
       
    flag = xor(k,bytes.fromhex(flag_enc))
    try:
        flag = flag.decode()
        print("Found flag (if it's not correct go press enter):", flag)
        input()
    except:
        pass
    
