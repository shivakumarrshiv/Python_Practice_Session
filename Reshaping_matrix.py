class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if (m * n == r * c) == False:
            return mat
        
        elements = []
        for i in range(m):
            for j in range(n):
                elements.append(mat[i][j])
        
        reshaped_matrix = []
        index = 0
        for i in range(r):
            row = []
            for j in range(c):
                row.append(elements[index])
                index += 1
            reshaped_matrix.append(row)
        
        return reshaped_matrix

# Input part
matrix = eval(input("Enter matrix: "))
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Reshaped Matrix:", Solution().matrixReshape(matrix, r, c))
