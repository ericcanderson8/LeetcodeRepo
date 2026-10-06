class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        output = 0
        for char in s:
            if char == ')':
                if count > 0:
                    count -= 1
                else:
                    output += 1
            else:
                count += 1

        output += count
        return output
        