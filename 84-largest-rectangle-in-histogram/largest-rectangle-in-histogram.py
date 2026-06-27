class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monoChromatic stack
        # means that for each increasing number, we will add it to the stack
        maxArea = 0

        stack = []
        for i in range(len(heights) + 1):
            # if new i is less than the stack, then we need to 
            while stack and (i == len(heights) or heights[i] < heights[stack[-1]]):
                item = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(heights[item] * width, maxArea)

            stack.append(i)
            # so I fully understand this problem now and I know I know how to attack it.
        return maxArea
         