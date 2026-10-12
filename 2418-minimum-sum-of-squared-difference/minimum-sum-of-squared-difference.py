class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Combine both lists into one 

        diffs = sorted((abs(a - b) for a, b in zip(nums1, nums2)), reverse=True)
        SIZE = len(diffs)
        diffs.append(0)

        k = k1 + k2 
        if k >= sum(diffs):
            return 0
        

        for i in range(SIZE):
            w = i + 1
            cost = w * (diffs[i]-diffs[i+1])
            if k >= cost:
                k -= cost
            else:
                level, extra = divmod(k, w)
                top = diffs[i] - level
                total = top * top * (w-extra) + (top-1) ** 2 * extra
                total += sum(d * d for d in diffs[i+1:SIZE])
                return total


        