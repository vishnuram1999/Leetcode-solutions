class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i == j:
                    res += mat[i][j]
                elif (i + j) == len(mat) - 1:
                    res += mat[i][j]

        return res
        