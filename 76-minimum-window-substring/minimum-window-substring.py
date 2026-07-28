class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # find the minimum substring that has all of t
        # keep track of a counter
        output = ""

        minLength = len(s)
        count = Counter(t)
        l = 0

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] -= 1
            
            while all(value <= 0 for value in count.values()):
                if len(output) == 0 or r + 1 - l < len(output):
                    output = s[l:r+1]

                if s[l] in count:
                    count[s[l]] += 1
                l += 1
        
        return output


