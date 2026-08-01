class Solution:
    def validate(self, s: str) -> bool:
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')' and count > 0:
                count -= 1
            elif s[i] == ')' and count == 0:
                return False
        if count > 0:
            return False
        return True       

    def removeInvalidParentheses(self, s: str) -> List[str]:
        # how do you even do breadth first search on a problem like this 
        layer = set()
        layer.add(s)

        newLayer = set()

        output = set()

        while len(output) == 0:
            for s1 in layer:
                if self.validate(s1):
                    output.add(s1)
                if len(output) == 0:
                    for i in range(len(s1)):
                        newLayer.add(s1[:i] + s1[i+1:])
            layer = newLayer
            newLayer = set()
        
        return list(output)

        # create a function to validate string is valid
        # you can use a stack to verify it is valid

            
