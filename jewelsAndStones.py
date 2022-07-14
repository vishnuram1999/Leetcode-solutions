class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for i in stones:
            if i in list(jewels):
                res += 1
        return res