class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # find the difference of the constant 

        q = deque()
        output = float('-inf')
        # yj + xj + (yi - xi) doesn't change
        for x,y in points:
            # add xj to points 
            # store value (val, x) cuz we have to ensure differences in x are <= k
            while q and  x - q[0][1] > k:
                q.popleft()

            if q:
                output = max(output, x + y + q[0][0])

            val = y - x
            while q and q[-1][0] < val:
                q.pop()
            q.append((val, x))

        return output



        