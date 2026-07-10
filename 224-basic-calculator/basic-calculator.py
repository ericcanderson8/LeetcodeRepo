class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        total = 0
        lastNum = 0
        sign = 1


        stack = [] # value & sign will go onto the like (val, sign)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append((total, sign))
                total = 0
                sign = 1
                lastNum = i+1

            if s[i] == "+" or s[i] == "-" or s[i] == ")":
                if i - lastNum > 0:
                    total += int(s[lastNum:i]) * sign
                if s[i] == "+":
                    sign = 1
                else:
                    sign = -1
                lastNum = i+1
            
            if s[i] == ")":
                newVal, sign = stack.pop()
                total = newVal + total * sign

            
        
        # if last char is ) we do somethign else tho
        if s[-1] == ")":
            return total
        else:
            total += int(s[lastNum:]) * sign
        
        return total
