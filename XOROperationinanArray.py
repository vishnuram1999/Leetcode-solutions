class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        for i in range(1, n):
            val = start + 2 * i
            ans = ans ^ val
        return ans
