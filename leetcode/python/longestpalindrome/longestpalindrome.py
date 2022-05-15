# https://leetcode.com/problems/longest-palindromic-substring/
import math


class Solution:
    def longestPalindrome(self, s):
        palind = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    if len(s[i:j+1]) > len(palind):
                        palind = s[i:j+1]
        return palind

    def isPalindrome(self, s):
        for i in range(math.floor(len(s)/2)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True


if __name__ == '__main__':
    a = "aaaa"
    b = "cbbd"
    c = "a"
    s = "ac"
    result = Solution().longestPalindrome(a)
    print(result)
