class Solution:
    def reverseBits(self, n: int) -> int:
        ans = bin(n)[::-1].split('b')[0]
        ans += '0'*(32-len(ans))
        return int(ans, 2)