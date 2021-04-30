# https://leetcode.com/problems/generate-parentheses/
def generateparentheses(n):
    stack = []
    res = []

    def backtrack(openN, closeN):
        if openN == closeN == n:
            res.append("".join(stack))
            return
        
        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closeN)
            stack.pop()

        if closeN < openN:
            stack.append(")")
            backtrack(openN, closeN + 1)
            stack.pop()

    backtrack(0, 0)
    return res

if __name__ == '__main__':
    # Example 1
    n = 3
    generateparentheses(n)