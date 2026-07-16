class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # number of people ith person can see to their right
        # I wonder if we can do some sort of thing

        # There must be some sort of data structure for this one
        # Monotonic stack
        # 5 8 10 
        # I see how this works now
        # For this problem we just add item to the stack removing items less than it first
        # we have 4
        # you start from the right, once you get an item that is larger
        # keep the array in sorted descreasing order, then get the smaller one to get the lenght of the list. 

        stack = []
        size = len(heights)
        output = [0 for i in range(size)]
        for i in range(size-1, -1, -1):
            if stack:
                count = 0
                if heights[i] > heights[stack[-1]]:
                    while stack and heights[i] > heights[stack[-1]]:
                        count += 1
                        stack.pop()
                if stack:
                    count += 1
                output[i] = count
            stack.append(i)
        
        return output


        