class Solution:
    def processStr(self, s: str) -> str:
        output = []
        for c in s:
            if c == '*':
                if len(output) > 0:
                    output.pop()
            elif c == '#':
                output = list(output) + list(output)
            elif c == '%':
                output = output[::-1]
            else:
                output.append(c)
        
        return "".join(output)
