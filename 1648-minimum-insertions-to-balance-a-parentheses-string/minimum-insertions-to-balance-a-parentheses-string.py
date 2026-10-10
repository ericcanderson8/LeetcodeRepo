class Solution:
    def minInsertions(self, s: str) -> int:
        
        output = 0
        count = 0
        for char in s:
            if char == '(':
                if count % 2 == 1:
                    output += 1
                    count -= 1
                count += 2
            elif char == ')':
                count -= 1
            if count == -1:
                output += 1
                count += 2
        
        output += count
        return output