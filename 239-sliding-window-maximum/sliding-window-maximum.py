class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if you see k numbers 
        SIZE = len(nums)

        q = deque()
        # append 
        # popleft
        output = []
        # k = 3
        # 0 1 2 3 i = 3 - k = 0
        # append tuple to dequeue (i, val)
        for i in range(SIZE):
            while q and q[0][1] < nums[i]:
                q.popleft()
            q.appendleft((i, nums[i]))

            while q[-1][0] <= i-k:
                q.pop()
            
            if i >= k-1:
                output.append(q[-1][1])
                
        return output

                

