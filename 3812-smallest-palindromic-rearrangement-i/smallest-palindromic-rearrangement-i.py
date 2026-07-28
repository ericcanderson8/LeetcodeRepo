class Solution:
    def smallestPalindrome(self, s: str) -> str:
        odd = len(s) % 2

        if len(s) == 0 or len(s) == 1:
            return s
        
        print(odd)

        string = list(s[:len(s)//2])
        string.sort()

        output = "".join(string)

        oddAdd = ""
        if odd:
            oddAdd = s[len(s)//2]
        output = output + oddAdd + output[::-1]
        print(string)
        
            
        return output
        