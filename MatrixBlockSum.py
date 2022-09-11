class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        fin = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res = 0
                p = max(i-k,0)
                q = max(j-k,0)
                u = min(i+k+1, len(mat))
                y = min(j+k+1, len(mat[0]))
                for l in range(p, u):
                    res += sum(mat[l][q:y])        
                fin[i][j] = res
        return fin
        