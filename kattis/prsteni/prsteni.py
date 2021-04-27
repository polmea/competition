# https://open.kattis.com/problems/prsteni
import sys

def main():
    n = int(input())

    rings = [int(x) for x in input().split()]
    first = rings[0]
    rings = rings[1:]

    for x in rings:
        print(str(first//gcd(first, x))+ "/" + str(x//gcd(first, x)))

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x


if __name__ == '__main__':
    main()