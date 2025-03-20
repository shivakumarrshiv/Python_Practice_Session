class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m = len(mat)
        n = len(mat[0])
        result = []

        diagonals = {}
        for i in range(m):
            for j in range(n):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                diagonals[i + j].append(mat[i][j])

        for d in range(m + n - 1):
            if d % 2 == 0:
                result.extend(reversed(diagonals[d]))
            else:
                result.extend(diagonals[d])

        return result


matrix = []
print("Enter matrix values row-wise (enter 'done' to stop):")
while True:
    row = input()
    if row.strip().lower() == 'done':
        break
    matrix.append(list(map(int, row.split())))

print("Diagonal Order:", Solution().findDiagonalOrder(matrix))






