# https://leetcode.com/problems/reverse-integer/
def romantoint(s):
    total = 0

    i = 0
    while i < len(s):
        currentindex = s[i]
        if currentindex == 'I':
            if i+1 != len(s):
                if s[i+1] == 'V':
                    total += 4
                    i += 1
                elif s[i+1] == 'X':
                    total += 9
                    i += 1
                else:
                    total += 1
            else:
                total += 1

        elif currentindex == 'X':
            if i+1 != len(s):
                if s[i+1] == 'L':
                    total += 40
                    i += 1
                elif s[i+1] == 'C':
                    total += 90
                    i += 1
                else:
                    total += 10
            else:
                total += 10

        elif currentindex == 'C':
            if i+1 != len(s):
                if s[i+1] == 'D':
                    total += 400
                    i += 1
                elif s[i+1] == 'M':
                    total += 900
                    i += 1
                else:
                    total += 100
            else:
                total += 100
        elif currentindex == 'V':
            total += 5
        elif currentindex == 'L':
            total += 50
        elif currentindex == 'D':
            total += 500
        elif currentindex == 'M':
            total += 1000
        else:
            return
        i += 1

    print(total)
    return total

if __name__ == '__main__':
    # Example 1
    s = "MCMXCIV"
    romantoint(s)