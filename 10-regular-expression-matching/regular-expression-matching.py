class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        cache = {}
        def dfs(i, j):
            if (i,j) in cache:
                return cache[(i,j)]

            if i >= len(s) and j >= len(p):
                return True
            
            if i <= len(s) and j >= len(p):
                print("False0")
                cache[(i,j)] = False
                return False
            

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')


            if j + 1 < len(p) and p[j+1] == '*':
                # two options
                if (match and dfs(i+1, j)) or dfs(i,j+2):
                    return True 
            
            else:
                if match:
                    return dfs(i+1, j+1)
            cache[(i,j)] = False
            return False
        
        return dfs(0,0)