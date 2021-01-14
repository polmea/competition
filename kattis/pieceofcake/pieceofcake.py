# https://open.kattis.com/problems/pieceofcake2
import sys

inputs = input().split()
n = int(inputs[0])
h = int(inputs[1])
v = int(inputs[2])

if n - h > h:
    h = n - h

if n - v > v:
    v = n - v

print(h*v*4)