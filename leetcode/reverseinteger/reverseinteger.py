# https://leetcode.com/problems/reverse-integer/
def reverseinteger(num):
    total = 0
    converted_num = str(num) 
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


if __name__ == '__main__':
    # Example 1
    exampleInteger = 901000
    reverseinteger(exampleInteger)