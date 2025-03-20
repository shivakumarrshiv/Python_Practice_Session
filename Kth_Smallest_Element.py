class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])  
        sortedList = []
        for i in range(m):
            for j in range(n):
                sortedList.append(matrix[i][j])
        sortedList.sort()
        return sortedList[k-1]
        
matrix = []
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter the matrix values row-wise:")
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

k = int(input("Enter target value: "))

print(f"The {k}th smallest Number is ", Solution().kthSmallest(matrix, k))