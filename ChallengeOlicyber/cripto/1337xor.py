flag_hex = "27893459dc8772d66261ff8633ba1e5097c10fba257293872fd2664690e975d2015fc4fd3c"


def xor(a, b):
    return bytes([ x ^ y for x,y in zip(a,b) ])

for i in range(255):
    if not chr(i).isprintable():
        continue
    # riusciamo a scoprire una parte della key grazie al known plaintext
    key = (bytes(x^y for x,y in zip(bytes.fromhex(flag_hex[:10]),(ord(c) for c in "flag{"))))
    key = (key + bytes([i]))*(len(flag_hex)//12 +1)
    if b'1337' in xor(bytes.fromhex(flag_hex),key):
        print(xor(bytes.fromhex(flag_hex),key))