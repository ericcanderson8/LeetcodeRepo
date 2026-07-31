class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # good subarray is where k is an index of the subbarry. 
        # begin from k then spread outwards for all parts that move up
        l = k
        r = k

        minNum = nums[k]
        output = 0

        while l >= 0 and r < len(nums):
            # compare it to the output
            output = max(output, (r-l+1) * minNum)

            if l > 0 and r < len(nums) - 1:
                if nums[l-1] > nums[r+1]:
                    l -= 1
                    minNum = min(minNum, nums[l])
                else:
                    r += 1
                    minNum = min(minNum, nums[r])
            elif l > 0:
                l-= 1
                minNum = min(minNum, nums[l])
            else:
                r+=1
                if r < len(nums):
                    minNum = min(minNum, nums[r])
        
        return output