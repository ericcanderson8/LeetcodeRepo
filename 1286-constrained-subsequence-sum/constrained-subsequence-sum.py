class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # k is the maximum you can jump, so I think that we will look at the maximum number in the k jump
        # we can keep track of the largest in the set going back using a dequeue where we just keep track of the largest, I think with k
        # the 

        q = deque()

        for i in range(len(nums)-1, -1, -1):

            while q and q[0] > i + k:
                q.popleft()
            

            if q:
                nums[i] += max(0, nums[q[0]])

            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

        return max(nums)
        