class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # you are combining these two numbers, but they cannot be the same.
        # you want to create the maximum number of that length
        # monotonic stack/ merging
        # for this problem I sort of have no idea
        # first loop is to do something 

        # select largest numbers in nums1 and nums2 based on the split
                    # create a function given a n return the largest number n
        output = []
        
        def largestN(array, n) -> list(int):
            if n == 0:
                return []
    
            stack = []
            drop = len(array) - n

            for num in array:
                while stack and stack[-1] < num and drop > 0:
                    stack.pop()
                    drop -= 1
                if len(stack) < n:
                    stack.append(num)
                else:
                    drop -= 1
            return stack
        
        def merge(A, B) -> list[int]:
            sizeA = len(A)
            sizeB = len(B)

            iA = 0
            iB = 0

            output = []

            while iA < sizeA or iB < sizeB:
                if iA < sizeA and iB < sizeB:
                    if A[iA] > B[iB]:
                        output.append(A[iA])
                        iA += 1
                    elif B[iB] > A[iA]:
                        output.append(B[iB])
                        iB += 1
                    elif B[iB] == A[iA]:
                        if B[iB:] > A[iA:]:
                            output.append(B[iB])
                            iB += 1
                        elif B[iB:] < A[iA:]:
                            output.append(A[iA])
                            iA += 1
                        else:
                            output.append(A[iA])
                            iA += 1
                elif iA < sizeA:
                        output.append(A[iA])
                        iA += 1
                elif iB < sizeB:
                        output.append(B[iB])
                        iB += 1
            return output

        for i in range(k+1):
            if len(nums1) >= k - i and len(nums2) >= i:
                output1 = largestN(nums1, k-i)
                output2 = largestN(nums2, i)

                combined = merge(output1, output2)
                output = max(output, combined)

            
        return output
                        
                        


                # remaining
                # find the best in both of these while 
            # Else continue
        
        # 0, 5
        # 1, 4
        # 2, 3
        # 3, 2
        # 4, 1
        # 5, 0