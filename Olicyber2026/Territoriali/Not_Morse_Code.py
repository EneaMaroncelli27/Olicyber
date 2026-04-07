with open('output.txt', 'r') as f:
    enc_flag = f.read()

last_one = "."
count = 0
flag =""
for c in enc_flag:
    if c != last_one:
        print(count)
        flag += chr(count)
        count = 1
    else:
        count += 1
    last_one = c
else:
    flag +=chr(count)
    
print(flag)