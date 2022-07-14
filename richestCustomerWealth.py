class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = {}
        for i in accounts:
            res[sum(i)] = i
        return max(res.keys())