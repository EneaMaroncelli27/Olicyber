from Crypto.Util.number import long_to_bytes, inverse
import sympy

n = 9565158649535229609530047362785645907094563351070470563788237
e = 65537
c1 = 6513402340379073542230710001434049959082564276254477896792619
c2 = 2739603094136133383923409703861575117091198809308633380325460

p,q = sympy.factorint(n).keys()

phi_n = (p - 1) * (q - 1)

d = inverse(e,phi_n)

m1 = pow(c1,d,n)
m2 = pow(c2,d,n)

flag = long_to_bytes(m1) + long_to_bytes(m2)

print(flag)