# https://open.kattis.com/problems/freefood
import sys

def main():
    n = int(input())
    days = []

    for i in range(n):
        line = input().split()
        interval = createInterval(int(line[0]), int(line[1]))
        for j in interval:
            if j not in days:
                days.append(j)

    print(len(days))

def createInterval(start, end):
    arr = []
    for i in range(end - start + 1):
        arr.append(start + i)
    return arr

if __name__ == '__main__':
    main()