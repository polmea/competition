# https://open.kattis.com/problems/deathstar

import sys

n = sys.stdin.readline()
n = int(n)

code = []

for i in range(n):
    code.append(0)

for j in range(n):
    line = sys.stdin.readline() 
    arr = line.split(' ')
    for k in range(n):
        curr = arr[k]
        if j == k:
            continue
        code[j] |= int(curr)
        code[j] |= int(curr)


for l in range(len(code)):
    print(code[l], end=" ")
