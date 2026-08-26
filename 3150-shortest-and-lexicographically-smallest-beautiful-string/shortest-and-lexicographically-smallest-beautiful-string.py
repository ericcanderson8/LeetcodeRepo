class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # first define what is a substring. 
        # have a queue, count the number of 1s in it
        q = deque()
        ones = 0
        output = ""

        for char in s:
            q.append(char)
            if char == '1':
                ones += 1
            
            if ones == k:
                print(q)
                curString = "".join(q)
                if output == "":
                    output = curString
                else:
                    print(output)
                    print(curString)
                    output = str(min(int(output), int(curString)))

                q.popleft()
                ones -= 1
            
            while q and q[0] == '0':
                q.popleft()
        
        return output
            
            # check if it is 
        