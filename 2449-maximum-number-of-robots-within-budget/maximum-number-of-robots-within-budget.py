class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        SIZE = len(chargeTimes)

        output = 0
        currentSum = 0
        qmCharge = deque()
        l = 0
        for i in range(SIZE):
            currentSum += runningCosts[i]
            while qmCharge and chargeTimes[qmCharge[0]] < chargeTimes[i]:
                qmCharge.popleft()
            qmCharge.appendleft(i)
            while qmCharge and qmCharge[-1] < l:
                qmCharge.pop()

            while qmCharge and chargeTimes[qmCharge[-1]] + (i - l+1) * currentSum > budget:
                currentSum -= runningCosts[l]
                while qmCharge and qmCharge[-1] == l:
                    qmCharge.pop()
                l += 1
            print(i, l)
            output = max(output, i-l+1)

        return output

            

            
            # run the calculation
            # if it is too large start removing from the left and recalculating everything

        
        return output