# https://leetcode.com/problems/reverse-integer/
def reverseinteger(x):
    total = 0
    converted_num = str(x) 
    multiplier = 1
    negative = False
    for i in range(len(converted_num)):
        currentindex = converted_num[i]
        if currentindex != '-': 
            current = int(currentindex)
            if current != 0:
                total += current*multiplier
                multiplier *= 10
            else:
                between = False
                if i+1 != len(converted_num):
                    for j in range(i+1, len(converted_num)):
                        newnumber = int(converted_num[j])
                        if newnumber != 0:
                            multiplier *= 10
                            break
        else:
            negative = True
    if negative == True:
        total *= -1
    
    if total < (-2**31) or total > (2**31 -1):
        total = 0
    print(total)
    return total

def reverseinteger_second(x):
    tem = int(str(x)[::-1])  if x > 0 else -int(str(abs(x))[::-1])

    if (tem < (-2**31) or tem > (2**31 -1)):
        tem = 0

    print(tem)
    return tem

if __name__ == '__main__':
    # Example 1
    exampleInteger = 901000
    reverseinteger_second(exampleInteger)