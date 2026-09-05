class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if len(nums) == 0:
            return -1

        maximum = nums[0]

        minStack = deque()
        for i, val in enumerate(nums):
            while minStack and minStack[-1][1] > val:
                minStack.pop()
            minStack.append((i,val))

        for i in range(len(nums)):
            maximum = max(maximum, nums[i])
            while minStack[0][0] < i:
                minStack.popleft()

            if maximum - minStack[0][1] <= k:
                return i
        
        return -1


        