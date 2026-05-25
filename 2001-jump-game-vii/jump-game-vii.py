class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # a sliding window that is behind
        if s[-1] == '1':
            return False

        currentTrue = 0
        SIZE = len(s)
        dp = [False] * SIZE
        dp[0] = True

        for i in range(SIZE):
            if i-minJump >= 0 and dp[i-minJump] == True:
                currentTrue += 1

            if i-maxJump - 1 >= 0 and dp[i-maxJump-1] == True:
                currentTrue -= 1
            
            if s[i] == '0' and currentTrue > 0:
                dp[i] = True
        
        if dp[-1] == True:
            return True
        return False
