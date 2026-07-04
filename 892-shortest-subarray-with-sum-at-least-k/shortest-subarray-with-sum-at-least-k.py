class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # return shortest subarray with the sum at least k
        # for this I think we just need a sliding window where the window is the sum k. 
        # so we will keep on increasing until we get to k length, 
        # When you add a new item, check how many items you can drop from the back of it, while still keeping it above k

        # we need to have a monotonic q
        # create a prefix sum tree

        prefix = [0]
        for i in nums:
            prefix.append(i + prefix[-1])
        
        output = len(nums) + 1
        q = deque()
        for i in range(len(prefix)):
            while q and prefix[q[-1]] > prefix[i]:
                q.pop()
            q.append(i)
            val = prefix[q[-1]] - prefix[q[0]]
            while val >= k:
                output = min(output,q[-1]-q[0])
                q.popleft()
                val = prefix[q[-1]] - prefix[q[0]]
        if output == len(nums) + 1:
            return -1
        return output
            




        
        