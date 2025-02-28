def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

mess1 = bytes.fromhex("d905e69ab6df68355136f501bf08f6b107aae602c38650") # flag^k1
mess3 = bytes.fromhex("0c47f394221a527a1523a3c2af9c37cff4324e976c4e79") # (flag^k1)^k2
mess2 = bytes.fromhex("b32e7469efaa4a23316609b078f1af1f9df1cff4c1bb54")  # flag^k2

k2 = xor(mess1,mess3) # (flag^k1)^[(flag^k1)^k2] = k2

print(xor(mess2,k2)) #(flag^k2) ^ k2 = flag