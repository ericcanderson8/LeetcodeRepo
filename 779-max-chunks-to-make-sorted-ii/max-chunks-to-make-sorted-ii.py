class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:

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

        for i, num in enumerate(arr):
            if (i == len(arr)-1) or prefixMax[i] <= prefixMin[i+1]:
                output += 1

        return output            
