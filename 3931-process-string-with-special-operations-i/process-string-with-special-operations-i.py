class Solution:
    def processStr(self, s: str) -> str:
        output = []
        for c in s:
            if c == '*':
                if len(output) > 0:
                    output.pop()
            elif c == '#':
                output.extend(output)
            elif c == '%':
                output.reverse()
            else:
                output.append(c)
        
        return "".join(output)
