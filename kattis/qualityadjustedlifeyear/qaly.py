# https://open.kattis.com/problems/qaly
import sys

n = int(input())
qaly = 0

for i in range(n):
    curr = input().split()
    qaly += float(curr[0])*float(curr[1])

print("%.3f" % qaly)