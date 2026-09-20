class Solution:
    def reverseDegree(self, s: str) -> int:
        # this is pretty simple
        print(123-ord('a'))
        print(123-ord('z'))

        output = 0
        for i, char in enumerate(s): 
            output += (123-ord(char)) * (i + 1)
        
        return output