from pwn import *
elf = ELF('./reversable')

import random, math, time

import sys
from copy import deepcopy


flag_len = 63
## 5 sono flag{ e l ultimo è }
payload = 'flag{' + 'a'*57 + '}'
idxs = [1, 2, 3, 4, 6, 8, 9, 0xA, 0xC, 0xE, 0xF, 0x10, 0x11, 0x14, 0x15, 0x16, 0x17, 0x18, 0x1A, 0x1B, 0x1C, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x2C, 0x2D, 0x2E, 0x30, 0x31, 0x32, 0x33, 0x36, 0x37, 0x38, 0x3A, 0x3B, 0x3D, 0x3E, 0x3F, 0x40, 0x42, 0x43, 0x45, 0x46, 0x47, 0x48, 0x4A, 0x4D, 0x4E, 0x4F]


for n in idxs:
    n = int(n)

print(f"{idxs=}")
print()
board = list("500003080003040000780000090001200000000001960007000032000400500002009000090120006")

# Create a 9x9 matrix
matrix = [board[i:i+9] for i in range(0, len(board), 9)]
## Using an online solver for sudoku
solved = [
    [5,4,9,7,6,3,2,8,1],
    [2,1,3,9,4,8,6,5,7],
    [7,8,6,5,1,2,3,9,4],
    [6,3,1,2,9,5,4,7,8],
    [8,2,4,3,7,1,9,6,5],
    [9,5,7,6,8,4,1,3,2],
    [1,7,8,4,3,6,5,2,9],
    [4,6,2,8,5,9,7,1,3],
    [3,9,5,1,2,7,8,4,6]
]
# Flatten the solved matrix into a single list
flattened_matrix = [str(num) for row in solved for num in row]
flag = 'flag{'
for idx in idxs:
    flag+= flattened_matrix[idx]
flag += '}'
print(flag)
