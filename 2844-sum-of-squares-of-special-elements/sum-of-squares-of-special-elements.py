class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        output = 0
        for i in range(n):
            if n % (i+1) == 0:
                output += (nums[i] * nums[i])   
        return output
        