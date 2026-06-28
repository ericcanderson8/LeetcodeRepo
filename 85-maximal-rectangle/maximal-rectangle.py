class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # for this problem I think that you can expand everything outward until you get somewhere
        # my thought here is that I look through every single point and I see how large of an areas it can hold
        # I just check going right and going down

        ROWS = len(matrix)
        COLS = len(matrix[0])

        newMatrix = [[0 for j in range(COLS)] for i in range(ROWS)]

        for i in range(ROWS-1, -1, -1):
            print(i)
            for j in range(COLS):
                if i == ROWS-1:
                    if matrix[i][j] == '1':
                        newMatrix[i][j] = 1
                    else:
                        newMatrix[i][j] = 0
                else:
                    if matrix[i][j] == '1':
                        newMatrix[i][j] = newMatrix[i+1][j] + 1
        

        def largestRectangleArea(heights: List[int]) -> int:
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
            return maxArea


        maxArea = 0
        for row in newMatrix:
            maxArea = max(maxArea, largestRectangleArea(row))
        
        return maxArea
