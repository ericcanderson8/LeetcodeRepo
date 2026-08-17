class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # to the right there is 1 smaller 
        # array mergesort 
        SIZE = len(nums)
        array = []
        def sort(val):
            index = bisect.bisect_left(array, val)
            array.insert(index, val)
            return index
             
        
        SIZE = len(nums)
        # insertion sort
        output = [0 for i in range(SIZE)]
        for i in range(len(nums)-1, -1, -1):
            index = sort(nums[i])
            output[i] = index

        return output
