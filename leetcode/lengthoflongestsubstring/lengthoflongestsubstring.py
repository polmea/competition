# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s):
        longest = ""
        for i in range(len(s)):
            current = ""
            for j in range(i, len(s)):
                if s[j] not in current:
                    current += s[j]
                    if len(current) > len(longest):
                        longest = current
                else:
                    if len(current) > len(longest):
                        longest = current
                    break
        
        return len(longest)
                
if __name__ == '__main__':
    a = "abcabcbb"
    b = "bbbbb"
    c = "pwwkew"
    d = "au"

    result = Solution().lengthOfLongestSubstring(d)
    print(result)