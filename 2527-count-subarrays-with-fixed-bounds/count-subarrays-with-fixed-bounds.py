class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # have an l and r
        # keep track of numbers ensuring minimum is equal to mink
        # keep track of numbers ensuring maximum is equal to maxk
        # here I think if you run into a number greater, you have to reset the distance

        min_idx = -1
        max_idx = -1
        bad_idx = -1

        output = 0
        for i in range(len(nums)):
            # if both min and max are above bad it will add the number inbetween the min and the bad
            if nums[i] == minK:
                min_idx = i
            if nums[i] == maxK:
                max_idx = i 
            if nums[i] > maxK or nums[i] < minK:
                bad_idx = i

            output += max(0,min(max_idx, min_idx) - bad_idx)
        return output


        
        