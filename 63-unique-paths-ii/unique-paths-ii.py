class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # this is a dp grid
        # += 1 in every possible area from the point you are at, that is wihtin the box

        HEIGHT = len(obstacleGrid)
        WIDTH = len(obstacleGrid[0])
        
        dp = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
        if obstacleGrid[HEIGHT-1][WIDTH-1] == 1:
            return 0

        dp[0][0] = 1

        for i in range(HEIGHT):
            for j in range(WIDTH):
                if obstacleGrid[i][j] == 0:
                    if i + 1 < HEIGHT and obstacleGrid[i+1][j] == 0:
                        dp[i+1][j] += dp[i][j]
                    if j + 1 < WIDTH and obstacleGrid[i][j+1] == 0:
                        dp[i][j+1] += dp[i][j]
        print(dp)
        return dp[HEIGHT-1][WIDTH-1]
            
