class Solution:
    def decodeString(self, s: str) -> str:
        output = ""
        i = 0
        while i < len(s):
            number = ""
            if s[i].isalpha():
                output += s[i]
            
            if s[i].isnumeric():
                while s[i].isnumeric():
                    number += s[i]
                    i += 1
                number = int(number)
                count = 1
                l = i
                while count > 0:
                    i += 1
                    if s[i] == '[':
                        count += 1
                    if s[i] == ']':
                        count -= 1
                for _ in range(number):
                    output += self.decodeString(s[l:i])
            i += 1

        return output
        