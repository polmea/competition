# https://leetcode.com/problems/two-sum/
def twosum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            print([lookup[target - num], i])
            return [lookup[target - num], i]
        lookup[num] = i


if __name__ == '__main__':
    # Example 1
    exampleList = [2,7,11,15]
    exampleTarget = 9
    twosum(exampleList, exampleTarget)