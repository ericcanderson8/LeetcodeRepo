class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # location of min, location of max
        # left and right
        # left to right
        # right to left
        if len(nums) == 1:
            return 1

        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))
        
        
        output = len(nums)
        output = min(output, max(maxIndex, minIndex) + 1)
        output = min(output, len(nums) - min(maxIndex, minIndex))
        output = min(output, (min(maxIndex, minIndex) + 1) + (len(nums) - max(maxIndex, minIndex)))

        return output


        