class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for i in range(n)]
        
        count = 1
        y, x = 0, 0
        matrix[0][0] = 1
        while count < n * n:
            while x+1 < n and matrix[y][x+1] == 0:
                x += 1
                count += 1
                matrix[y][x] = count
            while y+1 < n and matrix[y+1][x] == 0:
                y += 1
                count += 1
                matrix[y][x] = count
            while x-1 >= 0 and matrix[y][x-1] == 0:
                x -= 1
                count += 1                
                matrix[y][x] = count
            while y-1 >= 0 and matrix[y-1][x] == 0:
                y -= 1
                count += 1
                matrix[y][x] = count
            print(matrix)

        return matrix

            
        