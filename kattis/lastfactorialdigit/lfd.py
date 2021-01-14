# https://open.kattis.com/problems/lastfactorialdigit
import sys

def main():
    n = int(input())

    for i in range(n):
        curr = factorial(int(input()))
        currStr = str(curr)
        print(currStr[len(currStr)-1])


def factorial(n):
    fact = 1
    for i in range(1,n+1): 
        fact = fact * i 
    return fact

if __name__ == '__main__':
    main()