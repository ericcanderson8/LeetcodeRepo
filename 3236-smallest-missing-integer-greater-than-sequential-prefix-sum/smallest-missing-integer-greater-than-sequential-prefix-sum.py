class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # first add all elements to set

        elements = set()
        for num in nums:
            if num not in elements:
                elements.add(num)

        prev = -1
        count = 0
        for i in range(len(nums)):
            if i > 0 and nums[i]-1 == prev:
                count += 1
                prev = nums[i]
            elif i == 0:
                prev = nums[i]
                continue
            else:
                break
        
        total = 0
        for i in range(count+1):
            total += nums[i]

        print(count)
        print(total)

        while total in elements:
            total += 1

        return total