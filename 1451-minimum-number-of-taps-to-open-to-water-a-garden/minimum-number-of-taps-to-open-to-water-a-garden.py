class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # hardest step is saying where you can get from each n
        # pick maximum of all of the listed options available 

        launches = [-1] * (n + 1)
        for i, val in enumerate(ranges):
            if i - val < 0:
                launches[0] = max(launches[0], min(n, i + val))
            else:
                launches[i - val] = max(launches[i - val], min(n, i + val))
        
        count = 0
        currentEnd = launches[0]
        bestJump = 0
        for i in range(n+1):
            if i > bestJump:
                return -1

            if launches[i] > bestJump:
                bestJump = launches[i]
            
            if i == currentEnd:
                currentEnd = bestJump
                count += 1
        return count