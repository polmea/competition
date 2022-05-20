# https://leetcode.com/problems/palindrome-number/
import math

class Solution:
    def isPalindrome(self, s):
        if s < 0:
            return False
        elif s >= 0 and s < 10:
            return True
        else: 
            
            return True


if __name__ == '__main__':
    a = 121
    b = -121
    c = 10
    result = Solution().palindromeNumber(a)
    print(result)
