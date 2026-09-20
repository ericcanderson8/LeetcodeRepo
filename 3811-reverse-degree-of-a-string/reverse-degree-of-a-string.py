class Solution:
    def reverseDegree(self, s: str) -> int:

        output = 0
        for i, char in enumerate(s): 
            output += (123-ord(char)) * (i + 1)
        
        return output