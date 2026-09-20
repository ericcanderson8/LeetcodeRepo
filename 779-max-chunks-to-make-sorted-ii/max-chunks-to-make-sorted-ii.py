class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        # you can create an array to check min and max from left to right
        # you can go left to right

        # monotonic stack

        # thoughts on this problem create a montonic stack of min, 
        # if
        output = 0

        prefixMax = deque()
        for i in range(len(arr)):
            if not prefixMax or prefixMax[-1] < arr[i]:
                prefixMax.append(arr[i])
            else:
                prefixMax.append(prefixMax[-1])
        
        prefixMin = deque()
        for i in range(len(arr)-1, -1, -1):
            if not prefixMin or prefixMin[0] > arr[i]:
                prefixMin.appendleft(arr[i])
            else:
                prefixMin.appendleft(prefixMin[0])

        print(f"prefixMin: {prefixMin}")
        print(f"prefixMax: {prefixMax}")
        for i, num in enumerate(arr):
            if (i == len(arr)-1) or prefixMax[i] <= prefixMin[i+1]:
                print(i)
                output += 1


        # do you have one that is larger on the left side
        return output            
