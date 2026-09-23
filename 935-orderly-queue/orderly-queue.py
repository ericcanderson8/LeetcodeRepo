class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # this problem is very hard 
        size = len(s)

        if k == 1:
            smallest = s
            for i in range(size):
                if s[i:] + s[:i] < smallest:
                    smallest = s[i:] + s[:i]
            return smallest
        
        else:
            return "".join(sorted(s))
        