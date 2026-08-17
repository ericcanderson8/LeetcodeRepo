class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # deque
        # greedy array
        # first try to find the brute force solution, then see if you can do better than that. 

        # whenever you find a 0 just flip it, and see if it works. 
        # if not possible by the end then you will see. 

        # I am thinking I could create a bitmap
        q = deque()


        count = 0
        SIZE = len(nums)
        for i in range(SIZE):
            if q and q[0] == i:
                q.popleft()
            if (nums[i] == 0 and len(q) % 2 == 0) or (nums[i] == 1 and len(q) % 2 == 1):
                count += 1
                if i + k > SIZE:
                    return -1
                q.append(i+k)
        
        return count
