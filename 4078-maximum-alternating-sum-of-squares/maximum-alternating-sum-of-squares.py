class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted([x * x for x in nums])

        l = 0
        r = len(nums)-1
        output = 0
        while l <= r:
            output += nums[r] 
            if l < r:
                output -= nums[l]
            
            l += 1
            r -= 1
        
        return output

