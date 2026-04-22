enc_flag = bytes.fromhex("7971737c7e6d7866646f2c28712e7c2f2f717b402e2b7177292b40772e402a73402f71732f402867407b2c62")

f_half = ""
s_half = ""

for i in range(0,len(enc_flag),2):
    f_half += chr(enc_flag[i] ^ 31)
    s_half += chr(enc_flag[i+1] ^ 31)

print(f_half + s_half)
