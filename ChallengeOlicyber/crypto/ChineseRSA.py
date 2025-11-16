from Crypto.Util.number import bytes_to_long,long_to_bytes,inverse
from gmpy2 import iroot

ms = []
ys = []
def CRT(c:list,moduli:list):
    produttoria = 1
    x = 0
    for mods in moduli:
        produttoria*=mods # M = Produttoria da i a N di mi ---> m1*m2*m3
    for i in moduli:
        ms.append(produttoria//i) ## Mi --> M//mi
    for j in range(len(moduli)): 
        ys.append(inverse(ms[j],moduli[j])) ### yi = inverse(Mi) mod mi
    for k in range(len(moduli)):
        x = (x + c[k]*ms[k]*ys[k])%produttoria # x = Sommatoria ciphertext[i]*mi*yi mod M
    return x


ns = []
cs = []

with open('challenge.txt','r') as f:
    text = f.readlines()

for a in range(len(text)-1):
    if a%2 == 0:
        ns.append(int(text[a].split("=")[1].strip()))
    else:
        cs.append(int(text[a].split("=")[1].strip()))

me = CRT(cs,ns)
m = iroot(me,17)[0]
print(long_to_bytes(m).decode())