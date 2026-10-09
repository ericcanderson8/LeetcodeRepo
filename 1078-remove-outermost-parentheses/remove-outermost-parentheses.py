class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # first one from zero you have to remove
        # when it goes back to zero 
        count = 0
        output = []
        for i, char in enumerate(s):
            if char == '(':
                if count != 0:
                    output.append(char)
                count += 1
            else:
                count -= 1
                if count != 0:
                    output.append(char)
        
        return "".join(output)
        
            