from math import ceil
from Crypto.Util.number import long_to_bytes, inverse

n= 146652948863107767915515696389262268647958080423363432809510595078682568112085519929016552006340132750260244391442650419716209388476887752518821948643355769332931080957723170703642823372471212059667069985712741031890734368079274545006791082030796999444978356751235369237849185209094420930556569139123564127723
e= 65537
ct= 29866550050067643692473619455049192140190479758069897252295829267390344690107747214634468574079853475351608563312052986143110232253489826549882185837122231695139253296376749571108533659993018491393797757794110130200246559684585596096579385116077972392131805016636133672522654864012092864459984453971252224283

#Fermat preso da stack overflow, usabile perche p e q sono vicinissimi

# Source - https://stackoverflow.com/a
# Posted by John1024, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-16, License - CC BY-SA 3.0

def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def fermat(n, verbose=False):
    a = isqrt(n) # int(ceil(n**0.5))
    b2 = a*a - n
    b = isqrt(n) # int(b2**0.5)
    count = 0
    while b*b != b2:
        if verbose:
            print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2) # int(b2**0.5)
        count += 1
    p=a+b
    q=a-b
    assert n == p * q

    return p, q

p,q = fermat(n)

print("p =", p)
print("q =", q)

phi = (p-1)*(q-1)
d = inverse(e, phi)

m = pow(ct, d, n)
print(long_to_bytes(m))