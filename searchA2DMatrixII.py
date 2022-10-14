class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 1:
            if len(matrix[0]) == 1:
                if matrix[0][0] == target:
                    return True
            for x in range(0,len(matrix[0])):
                if matrix[0][x] == target:
                    return True
        for x in range(0,len(matrix)):
            if matrix[x][0] - target < 0 and matrix[x][-1] > target:
                for y in range(0,len(matrix[x])):
                    if matrix[x][y] == target:
                        return True
            elif matrix[x][0] == target or matrix[x][-1] == target:
                return True
        return False
