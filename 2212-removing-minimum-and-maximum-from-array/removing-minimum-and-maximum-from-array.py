class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # location of min, location of max
        # left and right
        # left to right
        # right to left
        if len(nums) == 1:
            return 1

        maximum = -(10 ** 5) -1. 
        minimum = 10 ** 5 + 1
        maxIndex = -1
        minIndex = -1

        for i in range(len(nums)):
            num = nums[i]
            if num > maximum:
                maximum = num
                maxIndex = i
            if num < minimum:
                minimum = num
                minIndex = i
        
        
        output = len(nums)
        output = min(output, max(maxIndex, minIndex) + 1)
        output = min(output, len(nums) - min(maxIndex, minIndex))
        output = min(output, (min(maxIndex, minIndex) + 1) + (len(nums) - max(maxIndex, minIndex)))

        return output


        