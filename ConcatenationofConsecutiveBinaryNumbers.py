class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ''
        for i in range(1, n+1):
            res += str(bin(i)).split("0b")[1]
        return int(res, 2) % (pow(10,9) + 7)
            
        