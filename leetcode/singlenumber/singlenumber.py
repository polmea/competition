# https://leetcode.com/problems/single-number/
def singlenumber(nums):
    lookup = []
    for i, num in enumerate(nums):
        if num not in lookup:
            lookup.append(num)
        else:
            lookup.remove(num)
    
    print(lookup[0])
    return lookup[0]



if __name__ == '__main__':
    # Example 1
    nums = [4,1,2,1,2]
    singlenumber(nums)