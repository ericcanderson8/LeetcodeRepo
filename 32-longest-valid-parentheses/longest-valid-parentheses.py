class Solution:
    def longestValidParentheses(self, s: str) -> int:

        SIZE = len(s)
        dp = [False for i in s]

        stack = []
        for i in range(SIZE):
            if s[i] == '(':
                stack.append(i)
            if stack and s[i] == ')':
                item = stack.pop()
                dp[i] = True
                dp[item] = True
        
        output = 0
        count = 0
        for entry in dp:
            if entry: 
                count += 1
            else:
                count = 0
            output = max(output, count)
        return output
        