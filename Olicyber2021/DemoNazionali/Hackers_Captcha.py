from operator import eq
from pwn import remote
from tqdm import trange
p = remote('hcaptcha.challs.olicyber.it', 20007)

max_chars = 20
num_map = {
    0:["_______   ","\\   _  \\  ","/  /_\\  \\ ","\\  \\_/   \\"," \\_____  /","       \\/ "],
    1:[" ____ ","/_   |"," |   |"," |   |"," |___|","      "],
    2:["________  ","\\_____  \\ "," /  ____/ ","/       \\ ","\\_______ \\","        \\/" ],
    3:["________  ","\\_____  \\ ","  _(__  < "," /       \\","/______  /","       \\/ "],
    4:["   _____  ","  /  |  | "," /   |  |_","/    ^   /","\\____   | ","     |__| "],
    5:[" .________"," |   ____/"," |____  \\ "," /       \\","/______  /","       \\/ "],
    6:["  ________"," /  _____/","/   __  \\ ","\\  |__\\  \\"," \\_____  /","       \\/ "],
    7:["_________ ","\\______  \\","    /    /","   /    / ","  /____/  ","          "],
    8:["  ______  "," /  __  \\ "," >      < ","/   --   \\","\\______  /","       \\/ "],
    9:[" ________ ","/   __   \\","\\____    /","   /    / ","  /____/  ","          "],
    "+":["          ","   .__    "," __|  |___","/__    __/","   |__|   ","          "],
    "-":["       ","       "," ______","/_____/","       ","       "],
    "*":["         "," /\\|\\/\\  ","_)    (__","\\_     _/","  )    \\ ","  \\/\\|\\/ "],
    "=":["       "," ______","/_____/","/_____/","       ","       "]
  
}


   
p.recvuntil(b'ricompensato\n')
for _ in trange(100):
    len_operandi = []
    i = 0
    eq = []
    nums = 0
    len_nums = []

    rows = []
    for n in range(6):
        row = p.recvline().decode()
        
        rows.append(row)
  
    while len(len_operandi)<3:
        ln = 0
        while  True:
            if rows[0][i] == " " and rows[1][i] == " " and rows[2][i] == " " and rows[3][i] == " " and rows[4][i] == " ":
                # print(f"found number {nums} lenght = {(ln)}")
                i += 1
                len_nums.append(i-sum(len_nums[nums:])-1) 
                nums +=1
                break
            ln += 1
            i += 1
        
        r0 = rows[0][len_nums[nums-1]-ln:i]
        r1 = rows[1][len_nums[nums-1]-ln:i]
        r2 = rows[2][len_nums[nums-1]-ln:i]
        r3 = rows[3][len_nums[nums-1]-ln:i]
        r4 = rows[4][len_nums[nums-1]-ln:i]
        r5 = rows[5][len_nums[nums-1]-ln:i]

        row = [r0[:-1],r1[:-1],r2[:-1],r3[:-1],r4[:-1],r5[:-1]]
        
        for n in num_map:
    
            if '\n'.join(row) in '\n'.join(num_map[n]):                
                if n == "+" or n == "-" or n == "*" or n == "=":
                    len_operandi.append(nums-1)

                eq.append(n)
                break
   
    n1 = 0
    j = len_operandi[0]-1
    
    for i in range(len_operandi[0]):
        n1 += eq[j]*10**i
        j -=1

    j = len_operandi[1]-1
    n2 = 0
    for i in range(len_operandi[0]+1,len_operandi[1]):
        n2 += eq[j]*10**(i-len_operandi[0]-1)
        j -=1
    n3 = 0
    j = len_operandi[2]-1
    for i in range(len_operandi[1]+1,len_operandi[2]):
        n3 += eq[j]*10**(i-len_operandi[1]-1)
        j -=1
    res1 = 1
    res2 = 1
    op1 = eq[len_operandi[0]]
    op2 = eq[len_operandi[1]]
    if op1 == '+' and op2 == '+':
        res1 = n1 + n2
        res2 = res1 + n3
    elif op1 == '+' and op2 == '-':
        res1 = n1 + n2
        res2 = res1 - n3
    elif op1 == '+' and op2 == '*':
        res1 = n2 * n3
        res2 = res1 + n1
    elif op1 == '-' and op2 == '+':
        res1 = n1 - n2
        res2 = res1 + n3
    elif op1 == '-' and op2 == '-':
        res1 = n1 - n2
        res2 = res1 - n3
    elif op1 == '-' and op2 == '*':
        res1 = -n2 * n3
        res2 = res1 + n1
    elif op1 == '*' and op2 == '+':
        res1 = n1 * n2
        res2 = res1 + n3
    elif op1 == '*' and op2 == '-':
        res1 = n1 * n2
        res2 = res1 - n3
    elif op1 == '*' and op2 == '*':
        res1 = n1 * n2
        res2 = res1 * n3

    p.sendlineafter(b'Risposta: ', str(res2).encode())
    rows.clear()
    
p.interactive()
   

