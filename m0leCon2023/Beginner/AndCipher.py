import requests

URL = 'http://andcipher.challs.olicyber.it/api/encrypt'

saved_bits = [] 

for i in range(100):
    r = requests.get(URL)
   
    s = bytes.fromhex(r.json()['encrypted'])
    bits = "".join(format(byte, '08b') for byte in s)
    saved_bits.append(bits)


flag_bits = saved_bits[0]
for bits in saved_bits[1:]:
    
    flag_bits = ''.join('1' if flag_bits[i] == '1' or bits[i] == '1' else '0' for i in range(len(flag_bits)))
   

print(bytes(int(flag_bits[i:i+8], 2) for i in range(0, len(flag_bits), 8)).decode())
  