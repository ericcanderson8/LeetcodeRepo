class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted(list(map(abs, nums)))

        l = 0
        r = len(nums)-1
        output = 0
        while l <= r:
            output += nums[r] * nums[r]
            if l < r:
                output -= nums[l] * nums[l]
            
            l += 1
            r -= 1
        
        return output

