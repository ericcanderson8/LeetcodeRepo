class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        slots = num
        count = 9
        output = ""

        if 9 * num < sum:
            return ""

        while count > 0 or sum > 0:
            divide = sum // count
            if divide > 0:
                sum -= (divide * count)
                for i in range(divide):
                    output += str(count)
                    slots -= 1
            count -= 1
        
        while slots > 0:
            output += "0"
            slots -= 1
        
        return output
        