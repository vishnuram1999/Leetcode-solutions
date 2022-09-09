class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = bin(n).split('b')[1].count('1')
        return ones