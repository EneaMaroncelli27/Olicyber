from Crypto.Util.number import long_to_bytes
import math
# d = e^-1 % phi da cui e*d-1 = k * phi dove k è un intero multiplo di phi

d = 2454147980105506786425977989549345389561620074780357800626167210119179432413932079707729534686888191626633148799840568097408265451820012752747703117155329
ea = 65537

k = ea*d-1

eb = 5
n = 11854178668350132536998770600021775412418919136267711466659575504833480429106340292308672916005731985811172925720279068992464220293573546887342858910065901
c = 11221865015245352586827949926936479339872912906868036678060873700351121339721754353868819679643501748382626251386036804928304376365191637409698833040968724

for i in range(1,100_000):
    if k % i != 0:
        continue

    phi = k // i
    peq = n - phi +1 ## possibili p e q  --> p+q= peq 
    # sistema
    # {p*q = N 
    # {p+q = peq

    # { p = peq-q
    # {peq-q*q = N
    # q**2 - peq*q +  N = 0 --> delta

    delta = peq**2 - 4*n ## 4ac
    rad = math.isqrt(delta)
    if rad**2 == delta:
        solutions = [(rad+peq)//2, (peq-rad)//2]
        if solutions[0] * solutions[1] == n:
        
            p = solutions[0]
            q = solutions[1]
            real_phi = phi
            break


d2 = pow(eb,-1,real_phi)
pt = pow(c,d2,n)
print(long_to_bytes(pt))