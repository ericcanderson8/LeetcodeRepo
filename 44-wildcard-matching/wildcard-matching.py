class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # i think I am going to structure this problem in the same way as the other problem, where I am going to a dfs
        clean_p = []
        for char in p:
            if char == '*' and clean_p and clean_p[-1] == '*':
                continue
            clean_p.append(char)

        p = clean_p

        cache = {}
        def dfs(i,j):

            if (i,j) in cache:
                return cache[(i,j)]
            # s can be at the end
            # p cannot be at the end
            if j >= len(p):
                return i >= len(s)
            
            match = i < len(s) and (p[j] == s[i] or p[j] == '?')
        
            if p[j] == '*':
                # skip it or include it
                cache[(i,j)] = dfs(i,j+1) or (i < len(s) and dfs(i+1,j))
            elif match:
                cache[(i,j)] = dfs(i+1,j+1)
            else:
                cache[(i,j)] = False
            
            return cache[(i,j)]

        return dfs(0,0)
