class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(1, n*2+1):
            if(i%n == 0 and i%2 == 0):
                return i
        