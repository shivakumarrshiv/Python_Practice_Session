class Solution:
    def checkMatrix(self, matrix:list[list[int]], target:int) ->bool:
        m = len(matrix)
        n = len(matrix[0])
        present = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    present= True
        if present:
            print("Present")
        else:
            print("Not Present")


matrix = []
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
print("Enter the matrix values row-wise:")
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)
target = int(input("Enter target value: "))
Solution().checkMatrix(matrix,target)

