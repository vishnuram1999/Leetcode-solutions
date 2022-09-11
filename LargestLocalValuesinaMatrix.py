class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        R = len(grid)
        C = len(grid[0])
        res = [[0 for x in range(R-2)] for y in range(C-2)] 
        for k in range(R-2):
            for h in range(C-2):
                maxi = 0
                for i in range(k,3+k):
                    for j in range(h,3+h):
                        if maxi < grid[i][j]:
                            maxi = grid[i][j]
                res[k][h] = maxi     
        return res
                
        
        
        
                
                
                
                