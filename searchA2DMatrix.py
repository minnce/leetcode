class Solution(object):
    def searchMatrix(self, matrix, target):
        foundValue = False
        tablePlace = -9999
        for x in range(0,len(matrix)):
            if matrix[x][0]-target <= 0 and matrix[x][-1]-target >= 0:
                tablePlace = x
                foundValue = True
                break
        if foundValue == True:
            for x in range(0,len(matrix[tablePlace])):
                if matrix[tablePlace][x] == target:
                    return True
        else:
            return False
