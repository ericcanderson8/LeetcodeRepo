class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums


        # Step 1 find pivot
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = nums[i]
                for j in range(len(nums)-1, -1, -1):
                    if nums[j] > pivot:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                nums[i+1:] = nums[i+1:][::-1]
                return 
        nums.sort()
                # we find our pivot is i
                # now we find next greater


        