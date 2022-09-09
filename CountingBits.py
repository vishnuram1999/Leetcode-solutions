class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            num = bin(i).split('b')[1]
            count = 0
            for i in range(len(num)):
                if num[i] == '1':
                    count += 1
            res.append(count)
        return res
            
        