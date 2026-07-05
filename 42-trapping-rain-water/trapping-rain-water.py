class Solution:
    def trap(self, height: List[int]) -> int:
        # this is just two pointers, keep track of left and right max height every time it goes down add water. 
        # this problem is fairly easy. 
        # I will do this one today. 

        l = 0
        r = len(height)-1
        maxL = height[0]
        maxR = height[-1]
        count = 0
        while l <= r:
            # always move the smaller one forward before the larger one. 
            minLR = min(maxL, maxR)
            print(f"L:{l}; R:{r}")
            if maxR < maxL: 
                newR = height[r]
                if newR < minLR:
                    count += minLR - newR
                    print(minLR - newR)
                if maxR < newR:
                    maxR = newR
                r -= 1
            else:
                newL = height[l]
                if newL < minLR:
                    count += minLR - newL
                    print(minLR - newL)
                if maxL < newL:
                    maxL = newL
                l += 1
        return count        