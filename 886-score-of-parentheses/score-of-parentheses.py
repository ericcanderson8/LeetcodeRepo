class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        values = [0]
        for char in s:
            if char == '(':
                values.append(0)
            else:
                current = values.pop()
                if current == 0:
                    current += 1
                else: 
                    current *= 2
                values[-1] += current
        
        return values[-1]

            