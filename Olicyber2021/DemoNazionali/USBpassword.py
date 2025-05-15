from Crypto.Util.number import bytes_to_long
import string
newmap = {
2: "PostFail",
4: "a",
5: "b",
6: "c",
7: "d",
8: "e",
9: "f",
10: "g",
11: "h",
12: "i",
13: "j",
14: "k",
15: "l",
16: "m",
17: "n",
18: "o",
19: "p",
20: "q",
21: "r",
22: "s",
23: "t",
24: "u",
25: "v",
26: "w",
27: "x",
28: "y",
29: "z",
30: "1",
31: "2",
32: "3",
33: "4",
34: "5",
35: "6",
36: "7",
37: "8",
38: "9",
39: "0",
40: "Enter",
41: "esc",
42: "\b",
43: "\t",
44: " ",
45: "_",
47: "{",
48: "}",
56: "/",
57: "CapsLock",
79: "RightArrow",
80: "LetfArrow"
}
myKeys = open("keys.txt")
i = 1
keys = []
active = 1
for line in myKeys:
    if "0" not in line:
        continue

    key = bytes.fromhex(line.strip().strip('"')[4:6])
    modif = line.strip().strip('"')[2:4]
    if key == b'\x00':
        continue
    try:
        if modif == "02":
            print(key)
            if newmap[bytes_to_long(key)] in string.ascii_lowercase:
                keys.append(newmap[bytes_to_long(key)].upper())
            elif newmap[bytes_to_long(key)] == "1":
                keys.append("!")
            elif newmap[bytes_to_long(key)] == "2":
                keys.append("@")
            elif newmap[bytes_to_long(key)] == "{":
                keys.append("{") 
            elif newmap[bytes_to_long(key)] == "{":
                keys.append("{")
            elif newmap[bytes_to_long(key)] == "}":
                keys.append("}")
            elif newmap[bytes_to_long(key)] == "_":
                keys.append("_")
            elif newmap[bytes_to_long(key)] == "/":
                keys.append("?")
            else:
                print("Key that u left ", bytes_to_long(key))
        else:
            if newmap[bytes_to_long(key)] == "CapsLock":
                active ^= 1
                continue
            if active == 1:
                keys.append(newmap[bytes_to_long(key)].upper())
            else:
                keys.append(newmap[bytes_to_long(key)])


            
            
    except Exception as e:
        # print("Error:", key," ", line)
        # print("Unworking key --> ", key)
        continue

keys = [" " if k == "space" else k for k in keys]
# 
print(''.join(keys))