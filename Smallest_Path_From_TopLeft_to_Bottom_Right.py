class Solution:
    def minPathSum(selc, grid: list[list[int]]) ->int:
        m = len(grid) 
        n = len(grid[0]) 

        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
        

        for j in range(1,n):
            grid[0][j] += grid[0][j-1]

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[m-1][n-1]


# Input part
grid = []
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter the grid values row-wise:")
for i in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

print("Minimum Path Sum:", Solution().minPathSum(grid))