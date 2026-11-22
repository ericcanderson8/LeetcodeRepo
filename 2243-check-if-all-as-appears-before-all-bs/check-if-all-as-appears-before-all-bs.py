class Solution:
    def checkString(self, s: str) -> bool:
        seenB = False
        for c in s:
            if c == 'b':
                seenB = True
            if c == 'a' and seenB == True:
                return False
        return True