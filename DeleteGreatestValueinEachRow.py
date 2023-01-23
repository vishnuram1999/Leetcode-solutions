class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = []
        while(len(grid[0])):
            ans1 = []
            for i in range(len(grid)):
                c =  max(grid[i])
                grid[i].remove(c)
                ans1.append(c) 
            ans.append(max(ans1))
        return sum(ans)
