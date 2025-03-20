class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        row = [0] * m
        columns = [0] * n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    columns[j] = 1
        
        for i in range(m):
            if row[i] == 1:
                for j in range(n):
                    matrix[i][j] = 0
        
        for j in range(n):
            if columns[j] == 1:
                for i in range(m):
                    matrix[i][j] = 0


# Input part
matrix = []
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter the matrix values row-wise:")
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

Solution().setZeroes(matrix)

print("Modified Matrix:")
for row in matrix:
    print(row)